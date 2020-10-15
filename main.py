import random
import json
from utilities import cmd

class Recipes:
    def __init__(self):
        self.data = self._load()
        self.type = ['Breakfast', 'Dinner', 'Supper']
        self.breakfast = list()
        self.dinner = list()
        self.supper = list()

        [self.breakfast.append(key) for key, _ in self.data['Breakfast'].items()]
        [self.dinner.append(key) for key, _ in self.data['Dinner'].items()]
        [self.supper.append(key) for key, _ in self.data['Supper'].items()]

    def _load(self):
        cmd.Window.clear()
        with open('recipes.json', 'r') as data:
            return json.load(data)

    def add(self, ingredients: list()):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)


class Week(Recipes):
    def __init__(self):
        self.days = {
            'Monday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}},
            'Tuesday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}},
            'Wednesday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}},
            'Thursday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}},
            'Friday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}},
            'Saturday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}},
            'Sunday':{'Breakfast':{}, 'Dinner':{}, 'Supper':{}}
        }
        super(Week, self).__init__()
        self._plan()

    def format(self):
        for index, (key, value) in enumerate(self.days.items()):
            if(index % 2 == 0): print(cmd.Color.red, end='')
            else: print(cmd.Color.cyan, end='')

            print(f'{key}:\n\
            Breakfast: {self.days[key]["Breakfast"]}\n\
            Dinner: {self.days[key]["Dinner"]}\n\
            Supper: {self.days[key]["Supper"]}\n', end='')
        print(cmd.Color.reset, end='')

    def _plan(self):
        for key, value in self.days.items():
            self.days[key]['Breakfast'] = random.choice(self.breakfast)
            self.days[key]['Dinner'] = random.choice(self.dinner)
            self.days[key]['Supper'] = random.choice(self.supper)


def main():
    week = Week()
    recipes = Recipes()
    week.format()

if __name__ == '__main__':
    main()
