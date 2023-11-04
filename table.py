def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end="\t")
        print()

# Replace 10 with the desired size of your multiplication table
multiplication_table(10)
