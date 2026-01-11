import socket
import json
import sys
import time
import threading

VERSION = "v1"
SEQ_NUM = 0

def register_with_directory(user_name, user_ip, user_port, dir_service_ip, dir_service_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = {
        "UID": user_name,
        "user IP": user_ip,
        "user PORT": user_port
    }
    sock.sendto(json.dumps(msg).encode(), (dir_service_ip, dir_service_port))

    response, _ = sock.recvfrom(1024)
    data = json.loads(response.decode())
    if data["error code"] == 400:
        print(f"Registered successfully: {data['destination IP']}:{data['destination port']}")
    else:
        print("Registration failed.")
    sock.close()

def lookup_destination(user_name, dir_service_ip, dir_service_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = {
        "User": user_name
    }
    sock.sendto(json.dumps(msg).encode(), (dir_service_ip, dir_service_port))

    while True:
        response, _ = sock.recvfrom(1024)
        data = json.loads(response.decode())
        if data["error code"] == 400:
            return data["destination IP"], data["destination port"]
        time.sleep(5)

def send_message(destination, user_name):
    global SEQ_NUM
    while True:
        message = input(f"{user_name}: ")
        msg = {
            "Version": VERSION,
            "Seq. num": SEQ_NUM,
            "UID": user_name,
            "DID": destination,
            "Message": message
        }
        sock.sendto(json.dumps(msg).encode(), destination)
        SEQ_NUM += 1

def receive_message(sock):
    expected_seq_num = 0
    while True:
        data, addr = sock.recvfrom(1024)
        msg = json.loads(data.decode())
        if msg["Seq. num"] == expected_seq_num:
            print(f"{msg['UID']} >> {msg['Message']}")
            expected_seq_num += 1

if __name__ == "__main__":
    user_name = sys.argv[1]
    source = sys.argv[2]
    target_user = sys.argv[3]
    dir_service = sys.argv[4]

    src_ip, src_port = source.split(":")
    dir_ip, dir_port = dir_service.split(":")
    
    register_with_directory(user_name, src_ip, int(src_port), dir_ip, int(dir_port))

    dest_ip, dest_port = lookup_destination(target_user, dir_ip, int(dir_port))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((src_ip, int(src_port)))

    threading.Thread(target=receive_message, args=(sock,)).start()

    send_message((dest_ip, int(dest_port)), user_name)
