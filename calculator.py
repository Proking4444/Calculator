user = input("What is your name?")
print("Hello", user)
opencalc = input("Would you like to use the calculator? (y/n)")
if opencalc.lower() in ["y", "yes"]:
    print("Opening Calculator...")
    model = input("Is your model 2D or 3D?")
    if model.lower() in ["2d", "2D"]:
        operation = input("What would you like to calculate?")
        if operation.lower() in ["perimeter", "Perimeter"]:
            length = input("What is the length of your rectangle?")
            width = input("What is the width of your rectangle?")
            print("The perimeter is:", float(length)*2 + float(width)*2)
        elif operation.lower() in ["area", "Area"]:
            length = input("What is the length of your rectangle?")
            width = input("What is the width of your rectangle?")
            print("The area is:", float(length)*float(width))
        else:
            print("You must choose an operation.")
    elif model.lower() in ["3d", "3D"]:
        operation = input("What would you like to calulcate?")
        if operation.lower() in ["surface area", "Surface Area"]:
            length = input("What is the length of your prism?")
            width = input("What is the width of your prism?")
            depth = input("What is the depth of your prism?")
            print("The surface area is:", float(length)*float(width)*2 + float(length)*float(depth)*2 + float(width)*float(depth)*2)
        elif operation.lower() in ["volume", "Volume"]:
            length = input("What is the length of your prism?")
            width = input("What is the width of your prism?")
            depth = input("What is the depth of your prism?")
            print("The volume is:", float(length)*float(width)*float(depth))
        else:
            print("You must choose an operation.")
    else:
        print("You must choose 2D or 3D.")
elif opencalc.lower() in ["n", "no"]:
    print("Terminating Application...")
    quit()
else:
    print("You must choose yes or no.")