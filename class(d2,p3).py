name= input("Enter your name")
length=len(name)
if length<=3:
    print("name must be at least 3 character")
elif length>=50:
    print("Name must be maximum of 50 words")
else:
    print("Name looks good")