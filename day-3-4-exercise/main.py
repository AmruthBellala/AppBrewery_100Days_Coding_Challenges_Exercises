# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25

Pepperoni_Small = 2
Pepperoni_Medium_Large = 3

Extra_Cheese = 1

if size == "L":
  bill = Large_Pizza
  if add_pepperoni == "Y":
    bill += Pepperoni_Medium_Large
  if extra_cheese == "Y":
    bill += Extra_Cheese
  print(f"Your final bill is: ${bill}.")
elif size == "M":
  bill = Medium_Pizza
  if add_pepperoni == "Y":
    bill += Pepperoni_Medium_Large
  if extra_cheese == "Y":
    bill += Extra_Cheese
  print(f"Your final bill is: ${bill}.")
elif size == "S":
  bill = Small_Pizza
  if add_pepperoni == "Y":
    bill += Pepperoni_Small
  if extra_cheese == "Y":
    bill += Extra_Cheese
  print(f"Your final bill is: ${bill}.")



