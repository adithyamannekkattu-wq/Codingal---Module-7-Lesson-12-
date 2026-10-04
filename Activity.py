class Cricket:
    def __init__(self, name, score):
        self.__name=name
        self.__score=score

    def info(self):
        print(f"Cricket:\nPlayer - {self.__name}\nScore - {self.__score}")

    def set_score(self, new_score):
        if new_score>0:
            self.__score+=new_score

        else:
            print("Invalid decrement")

class Football:
    def __init__(self, name, score):
        self.__name=name
        self.__score=score

    def info(self):
        print(f"Football:\nPlayer - {self.__name}\nScore - {self.__score}")

    def set_score(self, new_score):
        if new_score>0:
            self.__score+=new_score

        else:
            print("Invalid decrement")


football=Football("Adithya", 0)
cricket=Cricket("Jai", 0)

print("==============Sports Manager==============\n\n")

while True:

    choice=int(input("Choose any: \n1. See Info\n2. Set new score\n"))
    print("\n")

    if choice==1:
        for sport in (cricket, football):
            sport.info()
            print("\n")

    elif choice==2:
        sport=input("Choose a sport: cricket, football: ")
        new=int(input("Enter new score: "))

        if sport=="cricket":
            cricket.set_score(new)

        if sport=="football":
                football.set_score(new)




