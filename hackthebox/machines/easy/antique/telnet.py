#!/usr/bin/python3
import os
import sys
import socket
import threading
import subprocess
from _thread import *

welcome_message = b"""\nHP JetDirect\n\n"""

options = b"""
To Change/Configure Parameters Enter:
Parameter-name: value <Carriage Return>

Parameter-name Type of value
ip: IP-address in dotted notation
subnet-mask: address in dotted notation (enter 0 for default)
default-gw: address in dotted notation (enter 0 for default)
syslog-svr: address in dotted notation (enter 0 for default)
idle-timeout: seconds in integers
set-cmnty-name: alpha-numeric string (32 chars max)
host-name: alpha-numeric string (upper case only, 32 chars max)
dhcp-config: 0 to disable, 1 to enable
allow: <ip> [mask] (0 to clear, list to display, 10 max)

addrawport: <TCP port num> (<TCP port num> 3000-9000)
deleterawport: <TCP port num>
listrawport: (No parameter required)

exec: execute system commands (exec id)
exit: quit from telnet session
"""


HOST = '0.0.0.0'
PORT = 23

def threaded(conn):
	conn.send(welcome_message)
	conn.recv(1024)
	conn.send(b'Password: ')
	if b'P@ssw0rd@123!!123' in conn.recv(1024):
		conn.send(b'\nPlease type "?" for HELP\n')
		while True:
			conn.send(b'> ')
			data = conn.recv(1024)
			if b'?' in data:
				conn.send(options)
			elif b'exec' in data:
				cmd = data.replace(b'exec ',b'')
				cmd = cmd.strip()
				os.chdir('/var/spool/lpd')
				p = subprocess.Popen([f'{cmd.decode("utf-8")}'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				stdout,stderr=p.communicate()
				if stdout:
					conn.send(stdout)
			elif b'exit' in data:
				conn.close()
			else:
				conn.send(b'Err updating configuration\n')
	else:
		conn.send(b'Invalid password\n')
		conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST, PORT))
		s.listen()
		while True:
			conn, addr = s.accept()
			start_new_thread(threaded, (conn,))
		s.close()
