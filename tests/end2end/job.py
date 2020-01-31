import sys
import time

def main(name):
    time.sleep(1)
    print(f'My name is... {name}.')

main(sys.argv[1])
