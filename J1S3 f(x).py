'''
Write a Python program (.py file) that defines a function f(x)
that returns x**3 + 8. In the main() function of the program,
call f(x) with x = 9 and print the result.
Use an if statement that executes if the result is larger than 27
and prints “YAY!”. Use if __name__ == “__main__”: to setup the program for the command line
'''

def f(x):
    return x**3 + 8

def main():
    result = f(9)
    print(result)
    if result > 27:
        print("YAY!")

if __name__ == "__main__":
    main()
    
# Kevin Bozarth
