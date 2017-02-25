import socket, time
import aiohttp
import asyncio

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
message = b'Hello World!'
client.send(message)
time.sleep(0.2)
print('Received message:', client.recv(1024))
