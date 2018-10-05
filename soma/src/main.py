import json
import sys


def soma(a, b):
    return a + b

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(json.dumps({'soma': soma(x, y)}))
