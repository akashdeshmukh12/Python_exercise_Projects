
### Practice Python Program_P02 -->> Exercise "Use of Operators in Python for different Operations"

        ### Exercise -Take any two numbers and do different operations and find out results.


number_01 = int(input("take any two digit number you like for number_01 - "))
number_02 = int(input("take any two digit number you like for number_02 - "))
                                               # Input Function      -used to take any two numbers...[two_digit number]


sum = (number_01 + number_02)                  # Arithmatic Operator -used to addition of given two numbers, by user.

print(3*".\n")
print(f"total of given two numbers is {sum}")  # Print Function      -used to print/display outputs of operation.




        ### Exercise to add digits of 'sum' number [after addition of given two numbers].

#sum = total of given two numbers by user.

sum = str(sum)

first_digit =sum[0]
second_digit =sum[1]

Digit_sum = ((int(first_digit)) + (int(second_digit)))
print(f"total/addition of all digits of [total_number] is {Digit_sum}")
