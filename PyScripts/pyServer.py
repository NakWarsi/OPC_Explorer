import sys
sys.path.insert(0, "..")
import time
from opcua import ua, Server


if __name__ == "__main__":

    # setup the server
    server = Server()
 
    uri = "opc.tcp://192.168.137.1:4840"
    server.set_endpoint(uri)
    idx = server.register_namespace(uri)
    
    # get Objects node,
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()

    server.start()
    print("server started")
    
    try:
        count = 0
        while True:
            time.sleep(3)
            count += 0.1
            myvar.set_value(count)
    finally:
        server.stop()
