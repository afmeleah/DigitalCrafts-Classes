class Pet:
    #The line above defines the Pet class

    def __init__(self, name, fullness = 50, happiness = 50, hunger = 5, mopiness = 5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []
#The above lines define the attributes provided to a instance of the Pet class

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def get_toy(self, toy):
        self.toys.append(toy)
#The methods above make use of the attribute values of the instance

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()
#The method above shows how classes can bundle attributes

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)

class CuddlyPet(Pet):
#CuddlyPet is now a subclass that inherits the methods and attributes from the Pets class.

    def __init__(self, name, fullness = 50, hunger = 5, cuddle_level = 1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
#super calls the init from the Pets class. the rest add to the cuddlypet sub.

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()
#new method specific to this subclass

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()
        #The above overrides the be_alive in Pets with the new method for the subclass




