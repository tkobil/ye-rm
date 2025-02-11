from dataclasses import dataclass

@dataclass
class Track:
    name: str
    artists: list[str]
    id: str
    uri: str

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.id == other.id