import math


def print_abc(u_l):
    if u_l == 'u':
        for i in range(26):
            print(chr (ord ('A') + i),end=" ")
    else:
        for i in range(26):
            print(chr (ord ('a') + i),end=" ")
    print()

def print_word(letter):
    words = list('angry beyond caring despite every freedom given here in just killing lies my next opportunistic power quest reviving slumbering titans unbinding vicious wretched xenobiotic yowling zombies'.split())
    print(words[ord(letter) - ord('a')])

def print_multiplication_table(n):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            print(i*j,end=' ')
        print()

def print_square(n):
    print(n*n)

def check_if_prime_number(n):
    for i in range(2,math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            print("not prime")
            return
    print("is prime")

method_number = int(input('''
press the number of the method you want to run:

1) print the abc in uppercase or lowercase
2) print a word starting with a specific letter
3) print N*N multiplication table
4) print square number of a given number
5) check if a given number is prime
'''))

match method_number:
    case 1:
        print_abc(input("enter l for lowercase or u for uppercase\n"))
    case 2:
        print_word(input("enter start letter in lowercase\n"))
    case 3:
        print_multiplication_table(int(input("enter an number\n")))
    case 4:
        print_square(int(input("enter an number\n")))
    case 5:
        check_if_prime_number(int(input("enter an number\n")))
