while True:
    try:
        int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a number")
print("Thank you for Entring a number")
