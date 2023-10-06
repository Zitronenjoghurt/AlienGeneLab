# This is a gene entry how its found in the gene library (genes.json).
class Gene:
    def __init__(self, id, description, min, max, part, type, effect, code) -> None:
        self.id = id
        self.description = description
        self.min = min
        self.max = max
        self.part = part
        self.type = type
        self.effect = effect
        self.code = code

    def from_dict(id, data):
        return Gene(
            id=id,
            description=data['description'],
            min=data['min'],
            max=data['max'],
            part=data['part'],
            type=data['type'],
            effect=data['effect'],
            code=data['code']
        )