# try except else finally

# some error are-- FileNotFoundError, IndexError, KeyError

# FileNotFoundError
# try:  # try if something is error then execute except
#     file=open("abc.txt")
#     dict={"key":"value"}
#     print(dict["key"])
# except FileNotFoundError: # if file not found then this execute and create file of given name
#     # print("error")
#     print("File created")
#     with open("abc.txt","w") as file:
#         file.write("hello buddy")
# except KeyError as errormessage:
#     print(f"{errormessage} not found")
# else:  # execute if try block execute
#     file_data=file.read()
#     print(file_data)
# finally:  # execute either any of above execute or not
#     file.close()
#     print("finally file closed")


# generate user-defined error --- raise keyword
# raise TypeError("this is error i generate")

height=float(input("Height: "))
weight=int(input("weight: "))
if height>3:
    raise ValueError("Human height show be umder 3 meter")

bmi=weight/height**2
print("bmi: ",bmi)

