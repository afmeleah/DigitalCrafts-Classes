# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
#Link to leetcode: https://leetcode.com/problems/fizz-buzz/


for n in range (1, 101):
    div_3 = ((n % 3) == 0)
    div_5 = ((n % 5) == 0)
    if div_3 and div_5:
        print("FizzBuzz")
    elif div_3:
        print("Fizz")
    elif div_5:
        print("Buzz")
    else:
        print(n)

