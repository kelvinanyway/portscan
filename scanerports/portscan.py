import socket

url = "passe a url do site que deseja procurar portas abertas"
ports = [20,21,22,80,443,445,3306,25,3389]

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.settimeout(0.1)
	code = client.connect_ex((url, port))
	if code == 0:
		print(port, "OPEN")