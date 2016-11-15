class Animal(object):
    """
    This class defines a generic animal object

    Attributes: Species, Domesticated, Diet
    """

    # in my __init__() function I am using "Hidden" attribute names
    # Other languages call these private attributes
    def __init__(self, species, domesticated, diet):
        self.__species = species            # The ___ in front of the name makes it hidden
        self.__domesticated = domesticated
        self.__diet = diet          # Values should be Carnivore, Herbivore, Omnivore

    def __str__(self):
        if self.__domesticated:
            return '{0}s are domestic {1}s.'.format(self.__species, self.__diet)
        else:
            return '{0}s are wild {1}s.'.format(self.__species, self.__diet)

        # setters and getters
        # Set methods set a value for a hidden attribute
        # get methos return the value of a hidden value

    def set_species(self, species):
        self.__species = species

    def get_species(self):
        self.__species


    def set_domesticated(self, domesticated):
        self.__domesticated = domesticated

    def get_domesticated(self):
        self.__domesticated


    def set_diet(self, diet):
        self.__diet = diet

    def get_diet(self):
        self.__diet


# The class dog inherits Animal
# A dog is also an Animal
class Dog(Animal):
    """
    attributes: name, breed
    inherited attribute: species, domesticated, diet
    """


    # When I initialize my object I need to make sure both parent and child attributes are set
    def __init__(self, name, breed):
        Animal.__init__(self, 'Dog', 'True', 'Carnivore')       # this statement inits parent attribute
        self.__name = name
        self.__breed = breed

    # this method overrides the parent class method
    def __str__(self):
        desc = 'Your dog, {0} is a {1}. '.format(self.__name, self.__breed)
        desc += Animal.__str__(self)
        return desc


    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        self.__breed

    def set_name(self, name):
        self.__species = name

    def get_name(self):
        self.__name

