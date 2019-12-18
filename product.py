class Product:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link
    
    def serialize(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "link" : self.link
        }
    
    def from_json(self, json_):
        self.name = json_["name"]
        self.price = json_["price"]
        self.link = json_["link"]