from dataclasses import dataclass

@dataclass
class Item:
    id: int
    weight_g: int
    color: str
    length_cm:int

    def validation(self):
        """Valida os dados da peça com base nas regras de negócio.
        Retorna uma lista de erros caso a peça esteja fora dos padrões."""
        
        errors = []

        if self.weight_g is None:
            errors.append("O peso é obrigatório")
        
        if self.weight_g < 95 or self.weight_g > 105:
            errors.append("Peça inválida. O peso deve estar entre 95 e 105 gramas")
        
        if self.color is None:
           errors.append("A cor é obrigatória")
        
        if self.color not in ["azul", "verde"]:
            errors.append("Peça inválida. A cor deve ser azul ou verde")
        
        if self.length_cm is None:
            errors.append("O tamanho é obrigatório")
        
        if self.length_cm < 10 or self.length_cm > 20:
           errors.append("Peça inválida. O tamanho deve estar entre 10 e 20 cm")
        
        return errors