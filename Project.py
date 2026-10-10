class Dog:
    def __init__(self, name, status):
        self.__name=name
        self.__status=status

    def info(self):
        print(f"Dog:\nName - {self.__name}\nStatus - {self.__status}")

    def set_status(self, new_status):
        self.__status=new_status

class Cat:
    def __init__(self, name, status):
        self.__name=name
        self.__status=status

    def info(self):
        print(f"Cat:\nName - {self.__name}\nStatus - {self.__status}")

    def set_status(self, new_status):
        self.__status=new_status

dog=Dog("Jogo", "healthy")
cat=Cat("Megumi", "Sick")

print("==============Pet Healthcare==============\n\n")

while True:

    choice=int(input("Choose any: \n1. See Info\n2. Set new status\n"))
    print("\n")

    if choice==1:
        for pet in (dog, cat):
            pet.info()
            print("\n")

    elif choice==2:
        status=input("Choose a pet: cat, dog: ")
        new=int(input("Enter new status: "))

        if status=="dog":
            dog.set_status(new)

        if cat=="cat":
                cat.set_status(new)




