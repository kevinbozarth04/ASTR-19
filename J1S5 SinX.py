'''
Write a Python program that writes out a table of the function sin(x) vs. x,
where x is tabulated between 0 and 2 with a thousand entries.
Follow the basic Python program structure,
including a main program function and the if __name__ == “__main__” setup.
'''
import math

def makeTable(startPt, endPt, numPts):
    step = (endPt - startPt) / (numPts - 1)
    #print(step)
    table = []
    for i in range(numPts):
        x = startPt + i * step
        y = math.sin(x)
        table.append((x, y))
    return table

def printTable(table):
    for x, y in table:
        print(f"x = {x}, y = {y}")

def main():
    startPt = 0
    endPt = 2
    numPts = 1000

    table = makeTable(startPt, endPt, numPts)
    printTable(table)

if __name__ == "__main__":
    main()

# Kevin Bozarth
