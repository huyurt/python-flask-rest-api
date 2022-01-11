
names = ["Hudayfe", "Yurt"]
for name in names:
    print(name)
for num in range(5):
    print(num)



grades = [35, 84, 57, 95, 90]
total = sum(grades)
amount = len(grades)
print(total / amount)




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)





number = 7

while True:
    user_input = input("Whould you like to play? (Y/n)")

    if user_input in ("N", "n"):
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("It's wrong!")

