import socket
import json

user_db = {}

def handle_registration(data, addr):
    msg = json.loads(data.decode())
    user_name = msg["UID"]
    user_ip = msg["user IP"]
    user_port = msg["user PORT"]
    
    user_db[user_name] = (user_ip, user_port)
    response = {
        "error code": 400,
        "destination IP": user_ip,
        "destination port": user_port
    }
    return json.dumps(response).encode()

def handle_lookup(data):
    msg = json.loads(data.decode())
    user_name = msg["User"]
    if user_name in user_db:
        user_ip, user_port = user_db[user_name]
        response = {
            "error code": 400,
            "destination IP": user_ip,
            "destination port": user_port
        }
    else:
        response = {"error code": 600}
    return json.dumps(response).encode()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind(('0.0.0.0', 2000))

    while True:
        data, addr = server_sock.recvfrom(1024)
        if "user IP" in json.loads(data.decode()):
            response = handle_registration(data, addr)
        else:
            response = handle_lookup(data)
        server_sock.sendto(response, addr)

if __name__ == "__main__":
    main()
