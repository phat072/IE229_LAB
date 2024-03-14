import string


def cau1():
    Sum = 0
    for x in range(1, 10001):
        Sum += x
    print(Sum)


def cau2():
    Sum = 0
    for x in range(1, 101):
        Sum += x ** 3 + 3 * x ** 2 + 5 * x + 9
    print(Sum)


def reverse(xlist):
    return xlist[::-1]


def cau3():
    Array = [1, 3, 5, 7, 8]
    print(reverse(Array))
    # number of elements
    n = int(input("Enter number of elements : "))

    # Below line read inputs from user using map() function
    a = list(map(str,
                 input("\nEnter the numbers : ").strip().split()))[:n]

    print("\nReverse list is - ", reverse(a))


def main():
    # cau1()
    # cau2()
    cau3()


if __name__ == '__main__':
    main()
