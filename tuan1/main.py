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


def reverse_hard(xlist):
    return xlist[::-1]


def reverse(xlist):
    res = []
    for i in xlist:
        res = [i] + res
    return res


def cau3():
    Array = [1, 3, 5, 7, 8]
    print(reverse(Array))
    # number of elements
    # n = int(input("Enter number of elements : "))

    # Below line read inputs from user using map() function
    a = list(map(str,
                 input("\nEnter the numbers : ").strip().split()))

    print("\nReverse list is - ", reverse(a))


def Got_Dua():
    print("YNEOS"[2 ** int(input()) % 24 < 9::2])


def Competition():
    # n = int(input())
    # k = int(input())
    # # Below line read inputs from user using map() function
    # a = list(map(int,
    #              input("\nEnter the numbers : ").strip().split()))[:n]
    # a.sort(reverse=True)
    # Sum = 0
    # b = [0] * len(set(a))
    # for i in range(n):
    #     b[a[i]] += 1
    #     if b[a[i]] > 0:
    #         del(a[i])
    #
    # print(a)
    n = int(input())
    k = int(input())

    # Get user input as a list of integers
    a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

    # Sort the list in descending order (optional, but efficient)
    a.sort(reverse=True)

    # Count occurrences of each value in a dictionary
    value_counts = {}
    for num in a:
        value_counts[num] = value_counts.get(num, 0) + 1

    # Filter out elements with counts exceeding k (more efficient)
    filtered_a = [num for num in a if value_counts[num] <= k]

    # Print the filtered list
    print(filtered_a)


def main():
    # cau1()
    # cau2()
    cau3()
    # Got_Dua()
    # Competition()


if __name__ == '__main__':
    main()
