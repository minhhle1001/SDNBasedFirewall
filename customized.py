#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller,RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=RemoteController)
info('*** Adding controller\n')
c0= net.addController('c0',controller=RemoteController, port=6633)
c1= net.addController('c1',controller=RemoteController, port=6655)
info('*** Adding Host\n')
h1=net.addHost('h1',ip='10.0.2.10')
h2=net.addHost('h2', ip='10.0.2.20')
h3=net.addHost('h3', ip='192.168.2.30')
h4=net.addHost('h4', ip='192.168.2.40')
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(c0, s1)
net.addLink(c1, s2)
net.addLink(s1, h1)
net.addLink(s1, h2)
net.addLink(s2, h3)
net.addLink(s2, h4)
#net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(s2, h1)


info('*** Starting network\n')
net.start()
#info('*** Testing connectivity\n')
#net.ping([d1, d2])
info('*** Running CLI\n')
CLI(net)
#info('*** Stopping network')
#net.stop()

