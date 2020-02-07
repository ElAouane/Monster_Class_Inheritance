from Monster_Class import *
#Monster Student class here
#Inherit from monster class

class Student_Monster(Monster_Class):
    #Def characteristics

    def __init__(self, name, strenght, scary_skills, uni_id, scary_subject):
        super().__init__(name, strenght, scary_skills,)
        self.uni_id = uni_id
        self.scary_skills = scary_subject


    #DEf behaviour
    def run(self):
        return 'Nope'
    def sport(self):
        return 'Nope'
    def reproduce(self):
        return 'd(>.<)b ..... eyyyyyyeewwwww'


# monster1 = Student_Monster(name='Monster1', strenght=2, scary_skills='Nope', uni_id=111, scary_subject='Unknown')
#
# print(monster1.name)
# print(monster1.strenght)
# print(monster1.scary_skills)
# print(monster1.uni_id)
# print(monster1.scary_skills)