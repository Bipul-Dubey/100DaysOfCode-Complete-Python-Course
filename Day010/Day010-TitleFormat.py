def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You didn't provide valid input."
    str=(f"Result: {f_name.title()} {l_name.title()}")
    return str


fname=input("Enter first name: ")
lname=input("Enter last name: ")
formated_name=format_name(fname,lname)
print(formated_name)