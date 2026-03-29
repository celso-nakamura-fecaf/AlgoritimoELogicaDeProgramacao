from dataclasses import dataclass, field

@dataclass
class StorageBox:
    """Representa uma caixa de armazenamento de peças aprovadas.
    Cada caixa possui capacidade máxima de 10 itens e é fechada
    automaticamente ao atingir esse limite."""
    
    id: int
    batch_number: str
    item_ids: list = field(default_factory=list)
    is_closed: bool = False

    MAX_ITEMS: int = 10

    def current_count(self):
        return len(self.item_ids)

    def has_space(self):
        return not self.is_closed and len(self.item_ids) < self.MAX_ITEMS
    
    def to_dict(self):
        return {
            "id": self.id,
            "batch_number": self.batch_number,
            "item_ids": self.item_ids,
            "is_closed": self.is_closed
        }

 