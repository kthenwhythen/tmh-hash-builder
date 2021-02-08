import pandas


class Items:
    def __init__(self, localization):
        self.parser_data = None
        self.data = pandas.DataFrame()
        self.update_data()
        self.item_names = []
        self.item_names_local = pandas.read_json(f'item_names_{localization}.json')
        for name in self.data['Name'].to_list():
            self.item_names.append(name)

    def update_data(self):
        self.data = pandas.read_csv('data.csv', index_col=0)
        print('Updated\n')

    def save_data(self):
        self.data.to_csv('data.csv')
        print('Saved\n')
