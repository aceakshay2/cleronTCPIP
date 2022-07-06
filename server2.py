
import sys
from time import sleep
print("User Current Version:-", sys.version)
from pyModbusTCP.server import ModbusServer , DataBank

class local_server:
    
    def __init__(self , ip_addr , port_num):
        self.ip_addr = ip_addr
        self.port_num = port_num
        self.server  = ModbusServer(self.ip_addr , self.port_num ,no_block = True)
        try:
            '''Runs a server as long as server.stop is called'''
            print("Start server....")
            self.server.start()
            print("Server is online")
            
        except Exception as e:
            print("Shutdown server....")
            server.stop()
            print("Server is offline")
            print(e)
            
        except KeyboardInterrupt:
            print("Shutdown server....")
            server.stop()
            print("Server is offline")
            print('KeyboardInterrupt')
    
    def stop(self):
        print("Shutdown server....")
        self.server.stop()
        print("Server is offline")
        
    def send_data(self , register_num , num):
        '''
        input : a register number example send_data(40001 , 21)
        return : True
        '''
        try:
            if(register_num>=30001)and(register_num<=30100):
                return DataBank.set_words(register_num-30001 , [num])
            elif(register_num>=40001)and(register_num<=40100):
                return DataBank.set_words(register_num-40001 , [num])
        except Exception as e:
            print(e)
            return e
    
    def receive_data(self , register_num):
        '''
        input : a register number example 40001
        return : None or list of size 1 with number example [32]
        '''
        try:
            if(register_num>=40001)and(register_num<=40100):
                return DataBank.get_words(register_num-40001)
            else:
                pass 
        except Exception as e:
            print(e)
            return e


cleron_server = local_server('192.168.3.42' , 12345)
while 1:
    try:
        addr = 40001
        data = 45
        print(cleron_server.send_data( addr , data))
        val = cleron_server.receive_data(addr)[0]
        print(f"Data in {40001} is {cleron_server.receive_data(40001)[0]}")
        print(f"Data in {40002} is {cleron_server.receive_data(40002)[0]}")
        sleep(1)
        print()
    except Exception as e:
        print(e)
        cleron_server.stop()
        break
