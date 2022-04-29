# Distributed shared memory
We have implemented distributed shared memory using Read Replication Algorithm. The methods that implement distributed shared memory are written in `dsmlib.py` and `lockserver.py`.

* `dsmlib.py` - It is to be imported in all the python scripts that make use of distributed shared memory.
* `lockserver.py` - It is used to maintain locks on variables that are shared among processes. 

## Environment Set Up
* We are using `Pyro5` library of python for communication. To install it, run `pip3 install Pyro5`.
* Start the Pyro nameserver - `python3 -m Pyro5.nameserver`.
* Start the lockserver - `python3 lockserver.py`
## Running the clients
* Create a text file and write the clients name in it. For example -
```
client1
client2
client3
...
...
...
```
* Run the clients with the following command - `python3 client`<i>n</i>`.py path_to_clients_name_file`. For example, `python3 client1.py ./client_list.txt`