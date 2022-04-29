import Pyro5.api
import threading
import sys

client_file = sys.argv[1]

clientsproxy = list()
with open(client_file) as f:
    for client_name in f:
        # print(client_name.strip())
        temp_client = Pyro5.api.Proxy("PYRONAME:"+client_name.strip())
        clientsproxy.append(temp_client)

lockserver = Pyro5.api.Proxy("PYRONAME:lockserver")

data_dic = {}
lock = {}
cur_client = sys.argv[0][:-3]
print(cur_client)

@Pyro5.api.expose
class shared_memory_client(object):
    def write_client(self,variable,value):
        global data_dic
        data_dic[variable] = [value,1]
    def read_client(self,variable):
        global data_dic
        data_dic[variable][2] = 0
        return data_dic[variable][0]
    def objectOwnershipCheck(self,variable):
        global data_dic   
        if variable in data_dic and data_dic[variable][1]:
            return True
        return False
    def invalidate(self,variable):
        global data_dic
        if variable in data_dic:
            data_dic.pop(variable)


def start_shared(client):
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(shared_memory_client)
    ns.register(client, uri)
    daemon.requestLoop()

server = threading.Thread(target=start_shared,args=(cur_client,),daemon=True)
server.start()


def read(variable):
    lockserver.read_lock(variable)
    if variable in data_dic:
        lockserver.read_unlock(variable)
        return data_dic[variable][0]
    for client in clientsproxy:
        if client.objectOwnershipCheck(variable):
            data_dic[variable] = [client.read_client(variable),0,0]
    lockserver.read_unlock(variable)
    if variable in data_dic:
        return data_dic[variable][0]

def write(variable,value):
    lockserver.write_lock(variable)
    if variable in data_dic and data_dic[variable][2]:
        data_dic[variable]=[value,1,1]
    else:
        for client in clientsproxy:
            client.invalidate(variable)
        data_dic[variable] = [value,1,1]
    lockserver.write_unlock(variable)

def check():
    global data_dic
    for k,v in data_dic.items():
        print(k,v)

def checkloop():
    while(not input("Press Enter to check cache else continue execution")):
        check()

def script_end():
    input("Press enter to end script")

input("Press Enter to program execution")