import subprocess
import os
import hashlib


def run(user_input):
    subprocess.call(user_input, shell=True)
    os.system("echo " + user_input)


def calc(expr):
    return eval(expr)


def weak(data):
    return hashlib.md5(data).hexdigest()
