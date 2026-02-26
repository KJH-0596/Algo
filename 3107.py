ip = input()

if ip.count(":") ==8:
    ip = ip.replace("::",":")

ip = ip.replace("::",(7-ip.count(":"))*":" + "::")
ip = ip.split(":")

for i in range(len(ip)):
    if len(ip[i]) < 4:
        ip[i] = (4-len(ip[i]))*'0'+ip[i]

print(":".join(ip))