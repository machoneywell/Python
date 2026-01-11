import socket
import json
import threading
import sys

VERSION = "v1"
SEQ_NUM = 0

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
    destination = sys.argv[2]
    source = sys.argv[3]

    dest_ip, dest_port = destination.split(":")
    src_ip, src_port = source.split(":")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((src_ip, int(src_port)))

    threading.Thread(target=receive_message, args=(sock,)).start()

    send_message((dest_ip, int(dest_port)), user_name)
