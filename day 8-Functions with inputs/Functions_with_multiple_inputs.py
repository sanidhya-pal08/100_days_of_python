#functions with multiple inputs
def greet_with(name,location):
    print(f"hello {name}")
    print(f"weather is good in {location} today")
greet_with("sanidhya","indore") #positional argument
greet_with(location="jaipur",name="sanidhya") #keyword argument