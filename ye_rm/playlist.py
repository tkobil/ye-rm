from dataclasses import dataclass

@dataclass
class Playlist:
    id: str
    name: str

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.id == other.id