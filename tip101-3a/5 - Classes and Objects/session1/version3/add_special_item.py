class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def add_item(self, item_name):
        valid_items = [
            "banana", "green shell", "red shell", "bob-omb",
            "super star", "lightning", "bullet bill"
        ]
        if item_name in valid_items:
            self.items.append(item_name)
