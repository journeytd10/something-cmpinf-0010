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
    school = input("What school do you attend?")
    if school == "Swanson":
      print("You are in the Engineering school")
    elif school == "Dietrich":
      print("You are in the school for Arts and Sciences")


  
  

if __name__ == "__main__":
    main()
    something()
    branch()
