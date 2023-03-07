#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


#Write your code below this line 👇
print("Welcome to the Bill-Split calculator")
t = input("What was the total bill? $")
p= input("What percentage tip would you like to give? 10,12, or 15? ")
s= input("How many people to split the bill? ")

final= round ((float (t) + float (t)* (float (p)/100))/int (s),2)
final1= "{:.2f}".format(final)
print(f"Each person should pay: {final1}")