class ticket:
    print("Train booking system")
    restart = str(input("Do you need anything more: "))
    def Ticket(self):
        restart:str ="y"
        while restart!=('No','N','n','no'):
            print("1.PNR status")
            print("2.Ticket reservation")
            option=int(input("Enter Option: "))
            if option==1:
                print("Your PNR status:")
            elif option==2:
                people = int(input("Enter number of people: "))
                name.l=[]
                age.l=[]
                sex.l=[]
                for p in range(people):
                    name = str(input("Enter your name: "))
                    age = int(input("Enter your age: "))
                    sex = input("Enter your sex: ")
                    name = l.append(name)
                    age = l.append(age)
                    sex = l.append(sex)
                    restart = str(input("Do you need anything more: "))
                    if restart in ('y','yes','Yes','Y'):
                        restart='y'
                    else:
                        x=0

                    print("\nTotal number of tickets:",people)
                    for p in range (1,people+1):
                        print("TIcket:",people)
                        print("Nmae:",name.l[x])
                        print("Age:",agel[x])
                        print("sex:",sexl[x])
                        x+=1


class showing:(ticket)
def show(self):
    print("Thank you")
    o=showing()
    o=Ticket()
    o=show()