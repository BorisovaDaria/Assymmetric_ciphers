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
sock.bind((HOST, PORT))
sock.listen(1)

b = 81

conn, addr = sock.accept()
g, p, A = pickle.loads(conn.recv(1024))
B = g ** b % p
K = A ** b % p
print(g, p, A)
print("K =", K)

conn.send(pickle.dumps(B))

msg = pickle.loads(conn.recv(1024))
print(msg)
print(decode(msg, K))

msg = "И тебе привет!"
msg = encode(msg, K)
conn.send(pickle.dumps(msg))

conn.close()
