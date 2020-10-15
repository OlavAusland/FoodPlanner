import random

class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = list()

    def add(self, ingredients: list()):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)




def main():
    print(random.randint(0, 10))

if __name__ == '__main__':
    main()
