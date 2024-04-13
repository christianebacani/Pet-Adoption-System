def petAdoptionSystem():
    totalPrice = 0

    while True:
        print("\nAVAILABLE PETS")
        print("1.) Dogs")
        print("2.) Cats")
        print("3.) Rabbits")
        print("4.) Guinea Pigs")

        userPetChoice = int(input("Enter the pet you want to adapt : "))

        price = 0

        if userPetChoice == 1:
            print("\nAVAILABLE BREEDS OF DOGS\t  PRICE")
            print("1.) Bichon Frise\t\tP 20,000")
            print("2.) Pomeranian  \t\tP 15,000")
            print("3.) Golden Retriever\t\tP 20,000")
            print("4.) Labrador Retriever\t\tP 25,000")
            print("5.) Beagle      \t\tP 20,000")
            print("6.) Siberian Husky\t\tP 35,000")
            print("7.) Chow Chow   \t\tP 25,000")

            userDogBreedChoice = int(input("Enter the breed of dog you want to adapt : "))

            if userDogBreedChoice == 1:
                price += 20000
            
            elif userDogBreedChoice == 2:
                price += 15000

            elif userDogBreedChoice == 3:
                price += 20000

            elif userDogBreedChoice == 4:
                price += 25000

            elif userDogBreedChoice == 5:
                price += 20000

            elif userDogBreedChoice == 6:
                price += 35000

            elif userDogBreedChoice == 7:
                price += 25000

            else:
                print("Invalid Choice!")
                continue
            pass

        elif userPetChoice == 2:
            print("\nAVAILABLE BREEDS OF CATS \t  PRICE")
            print("1.) American Curl          \tP 25,000")
            print("2.) British Shorthair      \tP 25,000")
            print("3.) Ragdoll                \tP 65,000")
            print("4.) Siamese                \tP 15,000")
            print("5.) Scottish Fold          \tP 25,000")
            print("6.) Persian                \tP 20,000")
            print("7.) Burmese                \tP 47,000")


            userCatBreedChoice = int(input("Enter the breed of cat you want to adapt : "))

            if userCatBreedChoice == 1:
                price += 25000

            elif userCatBreedChoice == 2:
                price += 25000

            elif userCatBreedChoice == 3:
                price += 65000

            elif userCatBreedChoice == 4:
                price += 15000

            elif userCatBreedChoice == 5:
                price += 25000

            elif userCatBreedChoice == 6:
                price += 20000

            elif userCatBreedChoice == 7:
                price += 47000

            else:
                print("Invalid Choice!")
                continue
            pass

        elif userPetChoice == 3:
            print("\nAVAILABLE BREEDS OF RABBITS\tPRICE")
            print("1.) Lop Rabbit               \tP 125")
            print("2.) Angora Rabbit            \tP 10,000")
            print("3.) Netherland Dwarf Rabit   \tP 3,500")
            print("4.) Flemish Giant Rabbit     \tP 15,000")
            

            userRabbitBreedChoice = int(input("Enter the breed of rabbit you want to adapt : "))

            if userRabbitBreedChoice == 1:
                price += 125

            elif userRabbitBreedChoice == 2:
                price += 10000

            elif userRabbitBreedChoice == 3:
                price += 3500

            elif userRabbitBreedChoice == 4:
                price += 15000

            else:
                print("Invalid Choice!")
                continue
            pass

        elif userPetChoice == 4:
            print("\nAVAILABLE BREEDS OF GUINEA PIGS\tPRICE")
            print("1.) American Sow                 \tP 2,800")
            print("2.) Swiss Boar                   \tP 12,500")
            print("3.) Silkie Boar                  \tP 6,500")
            print("4.) Abyssinian Sow               \tP 4,800")
            print("5.) Teddy Sow                    \tP 4,000")

            userGuineaPigBreedChoice = int(input("Enter the breed of guinea pig you want to adapt : "))

            if userGuineaPigBreedChoice == 1:
                price += 2800

            elif userGuineaPigBreedChoice == 2:
                price += 12500

            elif userGuineaPigBreedChoice == 3:
                price += 6500

            elif userGuineaPigBreedChoice == 4:
                price += 4800

            elif userGuineaPigBreedChoice == 5:
                price += 4000

            else:
                print("Invalid Choice!")
                continue
            pass

        quantity = int(input("Enter the quantity of pet you want to adopt : "))
        totalPrice += price * quantity
        userAdoptAgain = input("Do you want to adopt more pet (y/n)?: ").lower()

        if userAdoptAgain != "y":
            print("Total Price : P", totalPrice)
            userMoney = int(input("Enter your money here : P "))

            if userMoney < totalPrice:
                print("Insufficient Money!")
                continue
            else:
                change = userMoney - totalPrice
                print("Change : P", change)
                print("Please Proceed to the Counter for the documents of your pet!")
                break

def aboutUs():
    print("\n\t\tABOUT US")
    print("\nWelcome to Bacani`s Pet Adoption System, where love finds its forever home!")
    print("\nAt Bacani`s Pet Adoption System, we believe in the power of compassion and connection. Our")
    print("\nmission is simple yet profound: to unite deserving pets with loving families, creating lifelong")
    print("\nbonds of joy and companionship.\n")


def menu():
    print("Welcome to Bacani`s Pet Adoption System!")
    input("Press Enter to Start : ")

    while True:
        print("\n\tMENU")
        print("1.) Adopt a Pet")
        print("2.) About us")
        print("3.) Exit")

        userChoose = int(input("Enter your choice here : "))

        if userChoose == 1:
            petAdoptionSystem()

        elif userChoose == 2:
            aboutUs()

        elif userChoose == 3:
            exit()
    
        else:
            print("Invalid Choice!")
            continue

        print("THANK YOU FOR USING OUR SYSTEM!")
        break

menu()