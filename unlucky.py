# for number in range(1, 21):
#     if number == 4 or number == 13:
#         print(f"{number} is UNLUCKY!")
#     elif (number % 2) == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
#BETTER WAY TO DO:
for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")