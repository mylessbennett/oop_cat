class Cat:
    """ Give cats mealtime """

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return "Name: {}\nPreferred_food: {}\nMeal Time:: {}".format(self.name, self.preferred_food, self.meal_time)

    def eats_at(self):
        if self.meal_time > 12:
            self.meal_time = str((self.meal_time - 12)) + "PM"
        else:
            self.meal_time = str(self.meal_time) + "AM"
        return self.meal_time

    def meow(self):
        return "My name is {} and I eat {} at {}".format(self.name, self.preferred_food, self.eats_at())


sprinkles = Cat("Sprinkles", "tuna", 18)
bandit = Cat("Bandit", "cat food", 7)
#-------------------------------------------------------------------------------------------------------------------
sprinkles_meal = sprinkles.eats_at()
print(sprinkles_meal)

bandit_meal = bandit.eats_at()
print(bandit_meal)
#-------------------------------------------------------------------------------------------------------------------
sprinkles_meow = sprinkles.meow()
print(sprinkles_meow)

bandit_meow = bandit.meow()
print(bandit_meow)
