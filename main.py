import json
import subprocess
import time
import multiprocessing
import os
import rpc_pb2_grpc
import rpc_pb2

# Function to find the last port required and adding one
def identify_last_port_plus_one(json_objs, start_port):
    last_port_number = start_port
    for obj in json_objs:
        if obj["type"] == "branch":
            last_port_number += 1
    return last_port_number

#This function is used to run each branch process through multiprocessing
def start_branch(branch_port, obj, last_port_number_plus_one):
    command = f'python Branch.py {branch_port} {obj["id"]} "{obj["balance"]}" {last_port_number_plus_one}'
    return os.system(command)

if __name__ == "__main__":
    # Read the input file
    with open("input_10.json", "r") as f:
        input_data = json.loads(f.read())

    # Initial port numbers for branches and customers
    branch_port = 50051
    customer_port = 50051

    # Identify the last port number plus one based on the number of branch objects
    last_port_number_plus_one = identify_last_port_plus_one(input_data, branch_port)

    # Create branch processes
    branch_processes = []
    for obj in input_data:
        if obj["type"] == "branch":
            branch_process = multiprocessing.Process(target=start_branch, args=(branch_port, obj, last_port_number_plus_one))
            branch_processes.append(branch_process)
            print(f"Main.py - Branch process started at port {branch_port}")
            branch_port += 1

    # Start branch processes
    for branch_process in branch_processes:
        branch_process.start()

    # Delay to ensure branch processes start before customer processes
    time.sleep(3)

    #Ready the Output file to store a dictionary of json objects
    with open("Output1.json", "w") as f:
        f.write("[")

    with open("Output2.json", "w") as f:
        f.write("[")

    with open("Output3.json", "w") as f:
        f.write("[")

    # Start customer processes using subprocess.Popen
    for obj in input_data:
        if obj["type"] == "customer":
            customer_port = 50051 + int(obj["id"]) - 1 #Each port is adjusted based on the Customer ID
            command = f'python Customer.py {customer_port} {obj["id"]} "{obj["customer-requests"]}" "{last_port_number_plus_one-50051}'
            p = subprocess.run(command, shell=True)
            print(f"Main.py - Customer process started at port {customer_port}")
            time.sleep(2)
            # p.kill()

    # Adjust the output to enclose it correctly
    with open("Output1.json", "r") as f:
        file = f.read()
        

    file = file[:-1]
    file += "]"

    with open("Output1.json", "w") as f:
        f.write(file)

    # Close all the Branches
    for branch_process in branch_processes:
        branch_process.terminate()

    with open("Output2.json", "r") as f:
        file = f.read()

    file = file[:-1]
    file += "]"

    with open("Output2.json", "w") as f:
        f.write(file)

    with open("Output3.json", "r") as f:
        file = f.read()

    file = file[:-1]
    file += "]"

    with open("Output3.json", "w") as f:
        f.write(file)

    
