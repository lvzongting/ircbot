#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import socket
import string 
from geopy.geocoders import Nominatim

HOST="irc.freenode.net"
PORT=6667
NICK="pacman-bot3"
IDENT="pacman-bot3"
REALNAME="lzt-bot3"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
CHAN="#tuna"

geolocator = Nominatim()

print "Done loading geopy, joining channel"
# KEY = "crossroads"
# s.send("JOIN :%s %s\r\n" % (CHAN, KEY))
s.send("JOIN :%s\r\n" % CHAN)

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        lineparts=string.rstrip(line)
        lineparts=string.split(lineparts)

        print lineparts
        try:        
            if(lineparts[0]=="PING"):
                s.send("PONG %s\r\n" % lineparts[1])  
                print 'PONG %s' % lineparts[1]
            if(lineparts[3].startswith(':find')):
                place=lineparts[4]                               
                print place
                location = geolocator.geocode(place)
                print location.address
                s.send("PRIVMSG %s :%s\r\n" % (CHAN, location.address.encode('utf8')))
                s.send("PRIVMSG %s :%s %s,%s\r\n" % (CHAN, "location", str(location.latitude), str(location.longitude)))
            if(lineparts[4].startswith('find')):
                place=lineparts[5]                               
                print place
                location = geolocator.geocode(place)
                print location.address
                s.send("PRIVMSG %s :%s\r\n" % (CHAN, location.address.encode('utf8')))
                s.send("PRIVMSG %s :%s %s,%s\r\n" % (CHAN, "location", str(location.latitude), str(location.longitude)))
        except:
            pass
