import xmlrpc.client
import sys

host_address = sys.argv[1]
host_port = sys.argv[2]
uri = "http://" + host_address + ":" + host_port
s = xmlrpc.client.ServerProxy(uri)

x = int(sys.argv[3])
y = int(sys.argv[4])


print("{} + {} is {}".format(x, y, s.add(x, y)))
print("{} - {} is {}".format(x, y, s.sub(x, y)))
print("{} * {} is {}".format(x, y, s.mult(x, y)))
if y == 0:
    print("{} / {} is Infinity".format(x, y))
else:
    print("{} / {} is {}".format(x, y, s.div(x, y)))

print(s.servertime())
print(s.name())
print(s.help())
