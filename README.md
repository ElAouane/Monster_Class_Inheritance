# __Monster Project__
## **Project Description:Create a Parent Class and a Child class**
* Create and define attribute and methods of Parent Class(Monster_Class) :older_man:

**DEF Monster Class and Attributes**
````
#Define monster class
class Monster_Class():
    #   Define characteristich
    def __init__(self, name, strenght, scary_skills):
        self.name = name
        self.strenght = strenght
        self.scary_skills = scary_skills
````
** DEF Behaviour
````
class Student_Monster(Monster_Class):
    #Def characteristics

    def __init__(self, name, strenght, scary_skills, uni_id, scary_subject):
        super().__init__(name, strenght, scary_skills,)
        self.uni_id = uni_id
        self.scary_skills = scary_subject
````
* Create a Child class and inherit from the Parent class

**DEF CHILD CLASS**
````
class Student_Monster(Monster_Class):
    #Def characteristics

    def __init__(self, name, strenght, scary_skills, uni_id, scary_subject):
        super().__init__(name, strenght, scary_skills,)
        self.uni_id = uni_id
        self.scary_skills = scary_subject
````
**DEF behaviours**
````
    #DEf behaviour
    def run(self):
        return 'Nope'
    def sport(self):
        return 'Nope'
    def reproduce(self):
        return 'd(>.<)b ..... eyyyyyyeewwwww'
````
* Test the code and print the output

## **Blockers, Problems, Bugs, Solutions:**
* __Blockers:__ Try to remember the syntax of Super() to override the main `__init__` class.
* __Problems:__ N/A
* __Bugs:__ `101`The IDE took quiet a long time before to inherite correctly all the data and pass them to its child
* __Solutions:__
    * __Problems:__ N/A
    * __Bugs:__ `101` **PATIENCE**


## **Outcomes:**
The project now can link all the classes together.
The child class can collect info from the Parent class, override the `__init__` method adding new parameters which will make 
each student unique at school.