print("This is the weight converter programmed by Mr. Rohan Khadka")
choice= input("Enter  your choice (Kgs or Lbs)")
if choice=="Kgs":
    weight_in_Kgs= float(input("Enter your weight"))
    pound= weight_in_Kgs*2.205
    print(f"your weight is {pound} lbs")
elif choice=="Lbs":
    weight_in_Lbs= float(input("Enter your weight"))
    kgs= weight_in_Lbs*0.453
    print(f"your weight is{kgs} Lbs")
else:
    print("Invalid  input")