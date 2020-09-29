import shelve


class StateManager:
    def __init__(self, file):
        self.file = file

    def add_value_by_key(self, key, value):
        with shelve.open(self.file) as d:
            d[key] = value

    def get_value_from_key(self, key):
        with shelve.open(self.file) as d:
            if key in d:
                value = d[key]
                return value
            else:
                return False
