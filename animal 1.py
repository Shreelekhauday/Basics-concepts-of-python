class animal:
    def __init__(self,name,sound,color,breed,legs):
        self.animal_name=name
        self.animal_sound=sound
        self.animal_color=color
        self.animal_breed=breed
        self.animal_legs=legs
    def animal_sound(self):
         print(f"{self.animal_sound}")

    def animal_type(self):
        if self.animal_legs==4:
            print("It is a land animal")
            print(Cat.animal_name, Cat.animal_sound, Cat.animal_color, Cat.animal_breed, Cat.animal_legs)
            print(Dog.animal_name, Dog.animal_sound, Dog.animal_color, Dog.animal_breed, Dog.animal_legs)
        elif self.animal_legs<4:
            print(parrot.animal_name, parrot.animal_sound, parrot.animal_color, parrot.animal_breed, parrot.animal_legs)


        else:
            print("It is a aquarium animal")
            print(Fish.animal_name, Fish.animal_sound, Fish.animal_color, Fish.animal_breed, Fish.animal_legs)
Cat=animal("Cat","meow...meow","white","persian",4)
Dog=animal("Dog","bow...boww","brown","german_shepard",4)
Fish=animal("Fish","Hmm....hmmmm","brown","gold_fish",0)
parrot=animal("parrot","teee...teeee","green","cockatoo",2)
animal_legs=int(input('enter the no of legs'))
if(animal_legs==4):
    #Cat.animal_type()
    Dog.animal_type()
elif(animal_legs==2):
   parrot.animal_type()
else:
    Fish.animal_type()