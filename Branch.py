import grpc
import rpc_pb2
import rpc_pb2_grpc
from concurrent import futures
import sys
import time
import json

class Branch(rpc_pb2_grpc.RPCServicer):

    def __init__(self, id, balance, last_branch_port_plus_one):
        # Unique ID of the Branch
        self.id = id
        # Balance of the Branch
        self.balance = int(balance)
        # List of branch ports for propagation
        self.branch_ports = list(range(50051, last_branch_port_plus_one))
        self.branch_ports.remove(int(thisport))
        # List of Client stubs to communicate with other branches
        self.stubs = [self.create_stub(port) for port in self.branch_ports]
        # Logical Clock
        self.clock = 0
        #Output
        self.output = {"id": self.id, "type": "branch", "events": []}
        self.output3 = {"id": self.id, "customer-request-id": "", "type": "branch"}

    def create_stub(self, port):
        channel = grpc.insecure_channel('localhost:' + str(port))
        return rpc_pb2_grpc.RPCStub(channel)

    def MsgDelivery(self, request, context):
        interface = request.interface
        if interface == "query":
            return self.query(request)
        elif interface == "deposit":
            return self.deposit(request)
        elif interface == "withdraw":
            return self.withdraw(request)
        elif interface == "propagate_withdraw":
            self.balance -= request.money
            return self.query(request)
        elif interface == "propagate_deposit":
            self.balance += request.money
            return self.query(request)

    def Call(self, request, context):
        if request.stop:
            with open("Output2.json", "a") as f:
                f.write(json.dumps(self.output, indent=4))
                f.write(",")
        return rpc_pb2.Rep(
            stopped=True
        )

    def query(self, request):
        self.clock=max(self.clock,request.clock)+1
        print(printable_branch, " - QUERY, Updated Balance:", self.balance)
        if request.interface == "query":
            pass
        else:
            event_dict = {
                    "customer-request-id": request.id,
                    "logical_clock": self.clock,
                    "interface": request.interface,
                    "comment": "event_recv from branch " + str(request.bank_id)
                }
            self.output["events"].append(event_dict)

            for i in event_dict:
                self.output3[i] = event_dict[i]

            with open("Output3.json", "a") as f:
                f.write(json.dumps(self.output3, indent=4))
                f.write(",")

        return rpc_pb2.Reply(
            id=request.id,
            interface=request.interface,
            result="success",
            balance=self.balance,
            clock=self.clock
        )

    def deposit(self, request):
        self.clock=max(self.clock,request.clock)+1
        self.balance += request.money
        print(printable_branch, " - DEPOSIT, Updated Balance:", self.balance)
        event_dict = {
                "customer-request-id": request.id,
                "logical_clock": self.clock,
                "interface": request.interface,
                "comment": "event_recv from customer " + str(self.id)
            }
        
        for i in event_dict:
                self.output3[i] = event_dict[i]

        with open("Output3.json", "a") as f:
            f.write(json.dumps(self.output3, indent=4))
            f.write(",")

        self.output["events"].append(event_dict)
        self.propagate_deposit(request.money,request.id)
        return rpc_pb2.Reply(
            id=request.id,
            interface=request.interface,
            result="success",
            balance=self.balance,
            clock=self.clock
        )

    def withdraw(self, request):
        self.clock=max(self.clock,request.clock)+1
        event_dict = {
                "customer-request-id": request.id,
                "logical_clock": self.clock,
                "interface": request.interface,
                "comment": "event_recv from customer " + str(self.id)
            }
        
        for i in event_dict:
                self.output3[i] = event_dict[i]

        with open("Output3.json", "a") as f:
            f.write(json.dumps(self.output3, indent=4))
            f.write(",")

        self.output["events"].append(event_dict)
        if self.balance >= request.money:
            self.balance -= request.money
            print(printable_branch, "- WITHDRAW, Updated Balance:", self.balance)
            self.propagate_withdraw(request.money,request.id)
            return rpc_pb2.Reply(
                id=request.id,
                interface=request.interface,
                result="success",
                balance=self.balance,
                clock=self.clock
            )
        else:
            print(printable_branch, "- WITHDRAW, Updated Balance:", self.balance)
            self.propagate_withdraw(0,request.id)
            return rpc_pb2.Reply(
                id=request.id,
                interface=request.interface,
                result="failure",
                balance=self.balance,
                clock=self.clock
            )

    def propagate_withdraw(self, amount, id):
        counter = 1
        for stub in self.stubs:
            self.clock += 1
            if counter != self.id:
                counter += 1
            event_dict = {
                "customer-request-id": id,
                "logical_clock": self.clock,
                "interface": "propagate_withdraw",
                "comment": "event_sent to branch " + str(counter)
            }
            self.output["events"].append(event_dict)
            stub.MsgDelivery(
                rpc_pb2.Request(
                    id=id,
                    interface="propagate_withdraw",
                    money=amount,
                    clock=self.clock,
                    bank_id=int(self.id)
                )
            )
            counter += 1

    def propagate_deposit(self, amount, id):
        counter = 1
        for stub in self.stubs:
            self.clock += 1
            if counter != self.id:
                counter += 1
            event_dict = {
                "customer-request-id": id,
                "logical_clock": self.clock,
                "interface": "propagate_deposit",
                "comment": "event_sent to branch " + str(counter)
            }
            self.output["events"].append(event_dict)
            stub.MsgDelivery(
                rpc_pb2.Request(
                    id=1,
                    interface="propagate_deposit",
                    money=amount,
                    clock=self.clock,
                    bank_id=int(self.id)
                )
            )
            counter += 1

if __name__ == '__main__':
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Read command line arguments
    thisport = sys.argv[1]
    branchid = sys.argv[2]
    branchbalance = sys.argv[3]
    last_branch_port_plus_one = int(sys.argv[4])

    # Print statements for process start
    printable_branch = f"Branch@{thisport}"
    print(f"{printable_branch} - Main: Branch process started at port: {thisport} with ID: {branchid}, balance: {branchbalance} and LastBranchPort: {last_branch_port_plus_one}")
    
    branch = Branch(branchid, branchbalance, last_branch_port_plus_one)
    # Create the Branch server with ID and balance
    rpc_pb2_grpc.add_RPCServicer_to_server(
        Branch(branchid, branchbalance, last_branch_port_plus_one),
        server
    )
    server.add_insecure_port('localhost:' + thisport)
    server.start()
    
    # Keep the server running till it is closed in main.py
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)
