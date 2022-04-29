from collections import defaultdict
import Pyro5.api
import sys

writelock = defaultdict(int)
readlock = defaultdict(int)

@Pyro5.api.expose
class locks(object):
    def write_lock(self,variable):
        while(writelock[variable] or readlock[variable]):
            continue
        writelock[variable] = 1
        readlock[variable] = 1
    def write_unlock(self,variable):
        writelock[variable] = 0
        readlock[variable] = 0
    def read_lock(self,variable):
        while(writelock[variable]):
            continue
        readlock[variable] = 1
    def read_unlock(self,variable):
        readlock[variable] = 0


client = sys.argv[0][:-3]



daemon = Pyro5.server.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(locks)
ns.register("lockserver", uri)
print("Lockserver Ready...")
daemon.requestLoop()

