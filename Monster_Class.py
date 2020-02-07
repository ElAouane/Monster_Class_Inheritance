#Define monster class
class Monster_Class():
    #   Define characteristich
    def __init__(self, name, strenght, scary_skills):
        self.name = name
        self.strenght = strenght
        self.scary_skills = scary_skills

    #Define Behaviours
    def eat(self):
        return f'{self.name} is eating'

    def sleep(self):
        return f'{self.name} is sleeping'
    def pay_taxes(self):
        return f'{self.name} does not pay taxes'


hamza = Monster_Class(name='Hamza',strenght=2, scary_skills='No')

# print(hamza.name)
# print(hamza.strenght)
# print(hamza.scary_skills)