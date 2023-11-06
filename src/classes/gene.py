# This is a gene entry how its found in the gene library (genes.json).
class Gene:
    def __init__(self, id: int, description: str, min: int, max: int, part: str, type: str, effect: str, code: str, mandatory: bool) -> None:
        self.id = id
        self.description = description
        self.min = min
        self.max = max
        self.part = part
        self.type = type
        self.effect = effect
        self.code = code
        self.mandatory = mandatory

    def from_dict(id, data: dict) -> 'Gene':
        return Gene(
            id=id,
            description=data['description'],
            min=data['min'],
            max=data['max'],
            part=data['part'],
            type=data['type'],
            effect=data['effect'],
            code=data['code'],
            mandatory=data['mandatory']
        )