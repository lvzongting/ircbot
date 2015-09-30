#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import socket
import string 
from cStringIO import StringIO
import urllib
from PIL import Image

HOST="irc.freenode.net"
PORT=6667
NICK="pacman-bot2"
IDENT="pacman-bot2"
REALNAME="lzt-bot2"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
CHAN="#tuna"

print "Done loading imgur, joining channel"
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
            if(lineparts[3].startswith(':location')):
                #center = "-30.027489,-51.229248"
                center=lineparts[4]                               
                url = "http://maps.googleapis.com/maps/api/staticmap?center="+center+"&size=800x800&zoom=14&sensor=false"
                print url 
                buffer = StringIO(urllib.urlopen(url).read())
                #image = Image.open(buffer)
                t = open('1.jpg','wb')
                t.write(buffer.getvalue())
                t.close()
                f=os.popen("curl -F 'name=@1.jpg' https://img.vim-cn.com/")
                rsl=f.readlines()
                rsl = rsl[0].strip('\n')
                print rsl
                s.send("PRIVMSG %s :%s %s\r\n" % (CHAN, "/imglink", rsl.replace("https","http")))
            if(lineparts[4].startswith('location')):
                #center = "-30.027489,-51.229248"
                center=lineparts[5]                               
                url = "http://maps.googleapis.com/maps/api/staticmap?center="+center+"&size=800x800&zoom=14&sensor=false"
                print url 
                buffer = StringIO(urllib.urlopen(url).read())
                #image = Image.open(buffer)
                t = open('1.jpg','wb')
                t.write(buffer.getvalue())
                t.close()
                f=os.popen("curl -F 'name=@1.jpg' https://img.vim-cn.com/")
                rsl=f.readlines()
                rsl = rsl[0].strip('\n')
                print rsl
                s.send("PRIVMSG %s :%s %s\r\n" % (CHAN, "/imglink", rsl.replace("https","http")))
        except:
            pass
