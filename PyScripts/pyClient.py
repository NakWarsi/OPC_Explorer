import sys
sys.path.insert(0, "..")
import time
from opcua import ua, Client

if __name__ == "__main__":
    
    url="opc.tcp://192.168.137.1:4840"
    client = Client(url)
    print("server address set")
    client.connect()
    try:
        print("Client connected to OPC UA Server")
        root = client.get_root_node()
        print("Objects node is: ", root)
        while True:
            temp=client.get_node("ns=2;i=2")
            temp_value=temp.get_value()
            print(temp_value)
            time.sleep(3)
    finally:
        client.disconnect()
