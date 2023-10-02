class Gene:
    def __init__(self, id, description, min, max, part, type, effects, code) -> None:
        self.id = id
        self.description = description
        self.min = min
        self.max = max
        self.part = part
        self.type = type
        self.effects = effects
        self.code = code

    def from_dict(data):
        return Gene(
            id=data['id'],
            description=data['description'],
            min=data['min'],
            max=data['max'],
            part=data['part'],
            type=data['type'],
            effects=data['effects'],
            code=data['code']
        )