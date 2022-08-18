n = int(input(" Please Enter the Maximum Value : "))

for num in range(1, n + 1):
    temp = num
    reverse = 0

    while (temp > 0):
        x = temp % 10
        reverse = (reverse * 10) + x
        temp = temp // 10

    if (num == reverse):
        print("%d " % num, end='  ')