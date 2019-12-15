converged_numbers = [1]
steps_list = [[1]]
longest = 1
longest_index = 0

def collatz(number):
    steps = [number]
    original = number
    while number > len(converged_numbers):
        if number % 2 == 0:
            number /= 2
            steps.append(int(number))
        else:
            number = number * 3 + 1
            steps.append(int(number))
    converged_numbers.append(original)
    steps = steps + steps_list[int(number - 1)][1:]
    return steps

# Tested up to 10**7

for x in range(2, 10**7):
    print(x)
    steps_list.append(collatz(x))
    if len(steps_list[x - 1]) > longest:
        longest = len(steps_list[x - 1]) - 1
        longest_index = len(steps_list) - 1

print('We just converged ' + str(converged_numbers[len(converged_numbers) - 1]) + ' numbers!')
print('The largest number of steps taken was ' + str(longest) + ' from the number ' + str(longest_index + 1))
see_list = input("Would you like to see the steps taken for " + str(longest_index + 1) + "? (y/n) ")

if see_list == "y":
    print(steps_list[longest_index])
