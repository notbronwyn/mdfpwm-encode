str = string.pack("<Is1s1s1",...)
a = io.open("headers.bin","wb")
a:write(str)
a:close()