import math
class Food:
    def __init__(self,carbs, protein, fat):
        try:
            self.carbs = carbs
            self.protein = protein
            self.fat = fat
            if carbs <=0 or protein<=0 or fat<=0:
                raise ValueError("Greshno vuvedeni danni")
        except ValueError as e:
            print(f"Greshno vuvedeni danni {e}")
            raise
    def calories(self):
        return (self.carbs *4) + (self.protein*4) + (self.fat*9)

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def calories(self):
        total_calories = sum(ingredient.calories() for ingredient in self.ingredients)
        return total_calories
    def __str__(self):
        return self.name
while True:
    try:
        n = int(input("Vuvedete broq recepti (ot 4 do 15): "))
        if 4 < n < 15:
            break
        else:
            print("Spazvaite zadadenite stoinosti")
    except ValueError:
        print("Vuvedete cqlo chislo")
recepies = []
for i in range(n):
    try:
        recipe_name = input("Въведете името на рецептата: ")
        ingredients = []
        num_ingredients = input("Vuvedete broq na receptite: ")
        if num_ingredients<=0:
            print("V receptata trqbva da ima pone edna sustavka!")
            continue
        for i in range(num_ingredients):
            try:
                carbs = float(input("Vuvedete carbs: "))
                protein = float(input("Vuvedete protein: "))
                fat = float(input("Vuvedete fat: "))
                ingredients.append(Food(carbs, protein, fat))
            except ValueError:
                print("Vuvedete validni stoinosti!")
        recipe = Recipe(recipe_name, ingredients)
        recepies.append(recipe)
    except ValueError as e:
        print(f"Greshka pri suzdavaneto na receptata {e}")
        continue
for recipe in recepies:
    print(f"Recepta: {recipe}, Kalorii: {recipe.calories()}")