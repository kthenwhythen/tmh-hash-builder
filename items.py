import json
import pandas


class Items:
    def __init__(self):
        self.parser_data = None
        self.data = pandas.DataFrame()
        self.update_data()
        self.item_names = []
        for name in self.data['Name'].to_list():
            self.item_names.append(name)
        print(self.item_names)

    def update_data(self):
        self.data = pandas.read_csv('data.csv')
        print('Updated\n')

    def save_data(self):
        self.data.to_csv('data.csv')
        print('Saved\n')
