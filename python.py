
def ejerEnClase():
    a = 0
    b = 1
    c = 0
    for i in range (0,15):
        c = a + b
        print("el restultado de num mas num ",c)
        a = b
        b = c

# print(ejerEnClase())


def ejer1():
    num = 5
    for i in range(0,10):
        print(num)
        num -= 1

# print(ejer1())


def ejer2():
    num = 1
    for i in range(0,10):
        print(num)
        num = num + num

# print(ejer2())

def ejer3():
    num = 1
    for i in range(0,10):
        print(num)
        if(i % 2 == 0):
            num = num + 1
        else :
            num = num + 2
            

# print(ejer3())


def ejer4():
    cre = 9
    num = 17
    a = 0
    b = 1
    c = 0
    print(b)
    for i in range(0,2):
        c = a + b + b
        print(c)
        a = b
        b = c
    for i in range(0,6):
        print(num)
        num = num + cre
        cre = cre + 1

# print(ejer4())



def ejer6():
    dec = 10
    cre = 0
    num = 1
    print(num)
    for i in range(0,10) :
        if(i % 2 == 0):
            cre += 1
            num += cre
            print(num)
        else :
            dec -= 1
            num += dec
            print(num)

# print(ejer6())


