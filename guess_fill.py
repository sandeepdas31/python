capital="chennai"

print("You have four chances to predit the correct answer")

for i in range(1,5):

    print("chance", i)
    capital1=str(input("Enter the capital of Tamil Nadu"))
    capital1=capital1.casefold()

    if(capital==capital1):
        print("You entered the correct answer")
        break

    else:
        print("try again")
        print("you have ",4-i," chances left" )