class Allele:
    def __init__(self, id, value) -> None:
        self.id = id
        self.value = value

    def get_id(self):
        return self.id
    
    def get_value(self):
        return self.value