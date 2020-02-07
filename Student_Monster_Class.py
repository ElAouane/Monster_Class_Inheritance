from Monster_Class import *
#Monster Student class here
#Inherit from monster class

class Student_Monster(Monster_Class):
    #Def characteristics

    def __init__(self, name, strenght, scary_skills, uni_id, scary_subject= ['Geek']):
        super().__init__(name, strenght, scary_skills,)
        self.uni_id = uni_id
        self.scary_subject = scary_subject


    #DEf behaviour
    def run(self):
        return 'Nope'
    def sport(self):
        return 'Nope'
    def reproduce(self):
        return 'd(>.<)b ..... eyyyyyyeewwwww'
