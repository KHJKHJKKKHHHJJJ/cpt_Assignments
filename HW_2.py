total_sum = 0

def calculate_sum(index, numbers, total_sum):
    total_sum += numbers[index]
    if index == 0:
<<<<<<< HEAD
        print("Sum:", total_sum)
=======
        print('The sum of the input integers is ==> ', total_sum)
>>>>>>> 8bf5025362a9e9fd76f4b4aa73105afd778e6531
        return total_sum
    calculate_sum(index - 1, numbers, total_sum)

while True:
    numbers_list = []
    user_input = input("Enter integers separated by spaces ==> ")

    if user_input == 'done':
        print('Program terminated. Goodbye!')
        break
    else:
        user_input_split = user_input.split(' ')

    try:
        for num_str in user_input_split:
            numbers_list.append(int(num_str))
    except ValueError:
        print('Must enter integers separated by spaces')
        continue

    if len(numbers_list) == 1:
        print("Must enter more than one integer")
        continue

    calculate_sum(len(numbers_list) - 1, numbers_list, total_sum)
    break
<<<<<<< HEAD
=======
    
>>>>>>> 8bf5025362a9e9fd76f4b4aa73105afd778e6531
