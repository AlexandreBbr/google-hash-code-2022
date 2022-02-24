#!/bin/env python3

def main():
    f=open("a_example.txt", "w+")

    for i in range(1):
        f.write("3\n")
        f.write("WebServer\n")
        f.write("Bob Anna\n")
        f.write("Logging\n")
        f.write("Anna\n")
        f.write("WebChat\n")
        f.write("Maria Bob\n")
    f.close()

if __name__== "__main__":
    main()