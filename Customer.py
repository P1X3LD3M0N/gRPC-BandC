import grpc
import rpc_pb2
import rpc_pb2_grpc
import sys
import json

class Customer:
    def __init__(self, ID, events, thisport, last_customer):
        # Unique ID of the Customer
        self.id = ID
        # Events from the input
        self.events = events
        # List of received messages used for debugging purposes
        self.recvMsg = []
        # Port number for the current customer process
        self.thisport = thisport
        # Pointer for the gRPC channel
        self.channel = grpc.insecure_channel('localhost:' + str(thisport))
        # gRPC stub for calling the server process
        self.stub = self.createStub()
        # This is the last customer
        self.last = last_customer
        # This is the dictionary to construct the output process
        self.output = {"id": self.id, "type": "customer", "events": []}
        self.output3 = {"id": self.id, "customer-request-id": "", "type": "customer"}
        # Logical Clock
        self.clock = 0

    def createStub(self):
        return rpc_pb2_grpc.RPCStub(self.channel)

    def executeEvents(self):
        # Convert single quotes to double quotes to make the events JSON parsable
        self.events = self.events.replace("'", "\"")

        # Loop over all events
        for event in json.loads(self.events):
            self.clock += 1
            event_dict = {
                "customer-request-id": event["customer-request-id"],
                "logical_clock": self.clock,
                "interface": event["interface"],
                "comment": "event_sent from customer " + str(self.id)
            }
            for i in event_dict:
                self.output3[i] = event_dict[i]

            with open("Output3.json", "a") as f:
                f.write(json.dumps(self.output3, indent=4))
                f.write(",")
            request = rpc_pb2.Request(
                id=event["customer-request-id"],
                interface=event["interface"],
                money=event.get("money", 0),
                clock = self.clock,
                bank_id=0
            )
            response = self.stub.MsgDelivery(request)
            
            print(f"Customer@{self.thisport} - Response: {response}")

            self.output["events"].append(event_dict)

        return self.output

    def finished(self):
        if int(self.id) == self.last:
            response = self.stub.Call(rpc_pb2.Req(stop=True))
            if response:
                pass

if __name__ == '__main__':

    thisport = int(sys.argv[1])
    customer_id = sys.argv[2]
    customer_events = sys.argv[3]
    last_customer = int(sys.argv[4])
    print(f"Customer@{thisport} - Main: Customer process started at port: {thisport} with ID: {customer_id} and events: {customer_events}")
    
    c = Customer(customer_id, customer_events, thisport, last_customer)
    output = c.executeEvents()
    c.finished()

    with open("Output1.json", "a") as f:
        f.write(json.dumps(output, indent=4))
        f.write(",")
