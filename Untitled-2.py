def main():
    name = input("Enter your name: ")
    major = input("Enter major: ")
    print(f"Welcome to Pitt {name} as a {major} major!!")

def something():
    rate = input("Are you enjoying your time at the University? (y/n) ")
    if (rate == "y"):
        print("That is amazing! We hope you have a great year!")
    else:
        print("Oh no! Please check out our resources on our website.")
def branch():
    school = input("What school do you attend?").strip().lower()
    if school == "swanson":
        print("You are in the Engineering school")
    elif school == "dietrich":
        print("You are in the school for Arts and Sciences")
    elif school == "business":
        print("You are in the school for Business")
    elif school == "SCI":
        print("You are in the school for computing and information")
    



if __name__ == "__main__":
    main()
    something()
    branch()
