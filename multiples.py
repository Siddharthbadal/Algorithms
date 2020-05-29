def natural_numbers(num):
    total = 0
    for i in range(num):
        if (i % 3) == 0 or (i % 5) == 0:
            total = total + i
    print(total)


natural_numbers(1000)
