name=str(input("Please enter your name: "))
days_borrowed=int(input("Please enter number of days the book was borrowed: "))
days_late=int(input("Enter the number of days late to submit: "))
total_fine=0
if days_late==0:
    total_fine=0
elif 1<=days_late<=5:
    total_fine=days_late*5
elif 6<=days_late>=10:
    total_fine=days_late*10
else:
    total_fine=days_late*20
print("Student Library Record")
print("Name of the student:", name)
print("Number of days borrowed:", days_borrowed)
print("Number of days late:", days_late)
print("Total fine:", total_fine)
if days_borrowed>=30:
    print("__"*30)
    print ("Library privilages may be restricted")



