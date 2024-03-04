import os
import shutil
import io
import ffmpeg
import sys
import json
import subprocess
header = b'MDFPWM\003'
luaPath = shutil.which("lua")
if len(sys.argv) > 1:
    luaPath = sys.argv[1]
elif luaPath == None:
    luaPath = "C:\\ffmpeg\\bin\\lua.exe"
a = open("output.mdfpwm", "wb")
data = b''
os.system("convert.sh")

l = open("left.dfpwm", "rb")
r = open("right.dfpwm", "rb")
ld = l.read(6000)
rd = r.read(6000)
while ld and rd:
    data = data+ld
    data = data+rd
    ld = l.read(6000)
    rd = r.read(6000)
l.close()
r.close()

aa = open("meta.json","r")
loaded = json.loads(aa.read())
aa.close()
length = sys.getsizeof(data)
artist = loaded["artist"]
title = loaded["title"]
album = loaded["album"]

subprocess.run([luaPath,"pack.lua",str(length),artist,title,album], shell=True)

temp = open("headers.bin","rb")
songinfo = temp.read()
temp.close()
print(songinfo)

a.write(header)
a.write(songinfo)
a.write(data)

a.close()
os.remove("headers.bin")
