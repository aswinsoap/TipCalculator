print("Welcome to the tip calculator.")
billamount=float(input("What was the total bill:?  ₹"))
tip=int(input("what percentage tip would you like to give?:"))
numberofpeople=int(input("How many people to split the bill?"))

billaftertip =billamount + (billamount*tip)/100

billsplit= billaftertip /numberofpeople
billsplit= round(billsplit,2)
finalamount="{:.2f}".format(billsplit)
print(f"Each person should pay: ₹{finalamount}")