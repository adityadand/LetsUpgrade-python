start = 104200
end = 702648265
for num in range(start,end):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum +=digit **3
        temp //=10
        if num == sum:
            print("The first armstrong number is",num)
