def format_name(f_name,s_name):
    formatted_f_name=f_name.title()
    formatted_s_name=s_name.title()
    return f"{formatted_f_name} {formatted_s_name}"

first_name=input("enter your first name")
last_name=input("enter our last name lilnigg")
print(format_name(first_name,last_name))
    