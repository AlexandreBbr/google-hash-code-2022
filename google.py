#!/bin/env python3

def main():
    f=open("a_example.txt", "w+")

    for i in range(1):
        f.write("3 \tthree projects are planned\n")
        f.write("WebServer \tassignments for project WebServer\n")
        f.write("Bob Anna \tBob -> first role, Anna -> second role\n")
        f.write("Logging \tassignments for project Logging\n")
        f.write("Anna \t\tAnna -> first role\n")
        f.write("WebChat \tassignments for project WebChat\n")
        f.write("Maria Bob \tMaria -> first role, Bob -> second role\n")
    f.close()

if __name__== "__main__":
    main()