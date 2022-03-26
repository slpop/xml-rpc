from xmlrpc.server import SimpleXMLRPCServer
import sys
import time

address = sys.argv[1]
port_num = int(sys.argv[2])

server = SimpleXMLRPCServer((address, port_num))


def name():
    return address


def help():
    return "Supported Procedures:\nName\nServer Time\nAdd\nSubtract\nMultiply\nDivide\n"


def servertime():
    return time.strftime('%H:%M:%S')


def add(x, y):
    return x + y


def sub(x, y):
    return x-y


def mult(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y


server.register_function(name, "name")
server.register_function(help, "help")
server.register_function(servertime, "servertime")
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mult, "mult")
server.register_function(div, "div")
server.serve_forever()
