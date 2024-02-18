# for i in range(100)
#     if i == 7
#     print(str[i])

end_number = 100  # Set the desired end number

for number in range(1, end_number + 1):
    if number % 7 == 0 or '7' in str(number):
        print("Boom!")
    else:
        print(number)