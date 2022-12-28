list = []
while True:
    numbers = input("Please enter a number from the list. \nType \"exit\" to show the list: ")
    if numbers == "exit":
        break
    elif numbers not in list:
        list.append(int(numbers))
    elif numbers in list:
        continue
print(list)