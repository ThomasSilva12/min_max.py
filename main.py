num_of_integers = int(input("Enter the number of integers: "))

4largest = None
smallest = None

for i in range(num_of_integers):
    user_input = int(input("Enter an integer: "))

    if i == 0:
        largest = user_input
        smallest = user_input
    else:
        if user_input > largest:
            largest = user_input
        if user_input < smallest:
            smallest = user_input

print("Largest integer:", largest)
print("Smallest integer:", smallest)

