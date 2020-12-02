# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_name = name1.lower() + name2.lower()

T1_Count = new_name.count("t")
R1_Count = new_name.count("r")
U1_Count = new_name.count("u")
E1_Count = new_name.count("e")
Sum1  = T1_Count + R1_Count + U1_Count + E1_Count

L1_Count = new_name.count("l")
O1_Count = new_name.count("o")
V1_Count = new_name.count("v")
E1_Count = new_name.count("e")
Sum2 = L1_Count + O1_Count + V1_Count + E1_Count

Sum = str(Sum1) + str(Sum2)
Sum_int = int(Sum)

if Sum_int < 10 or Sum_int > 90:
  print(f"Your score is {Sum_int}, you go together like coke and mentos.")
elif Sum_int >= 40 and Sum_int <=50:
  print(f"Your score is {Sum_int}, you are alright together.")
else:
  print(f"Your score is {Sum_int}.")