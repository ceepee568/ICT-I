try:
    n=float(input("Enter a number: "))
    res=100/n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

except:
    print("An unexpected error occured.")

else:
    print("result is", res)

finally:
    print("Execution complete")
    

