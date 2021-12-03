from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.cli import CLI
import time

# Sets up network with two hosts connected to a switch 
topo = SingleSwitchTopo()
net = Mininet(topo=topo)

# Start the network
net.start()
net.pingAll()

nodes = net.items()
s = net.get('h1')
r = net.get('h2')

s.setIP('192.168.1.1', 24)
r.setIP('192.168.1.2', 24)

s.cmd('python3 s.py > out.txt &')
time.sleep(5)
result = r.cmd('python3 client.py')
print(result)

net.stop()  