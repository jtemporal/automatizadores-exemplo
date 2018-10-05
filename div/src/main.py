import json
import sys


def div(a, b):
    return a / b

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(json.dumps({'div': div(x, y)}))
