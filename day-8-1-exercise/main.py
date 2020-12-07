#Simple Function
def greet():
  print("Hello")
  print("How do you")
  print("This is 100 Days coding")
greet()

#Function that allows for input
#'name' is the parameter.
#'Amruth' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Amruth")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Amruth", "Nowhere")
#vs.
greet_with("Nowhere", "Amruth")


#Calling greet_with() with Keyword Arguments
greet_with(location="India", name="Amruth")