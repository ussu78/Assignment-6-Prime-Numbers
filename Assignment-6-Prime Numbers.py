def prime(n):
    list_prime = []
    for i in range(2, n+1):
        divider = 0
        for x in range(2, i):
            if not i % x:
                divider += 1
                break
        if not divider:
            list_prime.append(i)
    print(list_prime)


n = int(input("Enter a limit number : "))
prime(n)
