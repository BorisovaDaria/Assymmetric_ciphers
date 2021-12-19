import socket
import pickle

ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'


def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))

HOST = 'localhost'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 7, 52, 31
A = g ** a % p
sock.send(pickle.dumps((g, p, A)))
B = pickle.loads(sock.recv(1024))
K = B ** a % p
print("K =", K)

msg = "Привет!"
msg = encode(msg, K)
sock.send(pickle.dumps(msg))

msg = pickle.loads(sock.recv(1024))
print(msg)
print(decode(msg, K))

sock.close()