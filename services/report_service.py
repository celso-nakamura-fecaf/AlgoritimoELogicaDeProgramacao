from services.data_base_service import DataBaseService

class ReportService(DataBaseService):

    def generate(self):
        """Gera um relatório consolidado da produção.
        Exibe quantidade de peças válidas, inválidas,
        caixas completas e motivos de reprovação."""

        db = self._get_db()

        total_valid = len(db["items"])
        total_invalid = len(db["invalid_items"])
        total_closed_boxes = sum(
            1 for box in db["storage_boxes"] if box["is_closed"]
        )

        motivos = {
            "Peso fora do padrão": 0,
            "Cor inválida": 0,
            "Tamanho incorreto": 0,
            "Múltiplos erros": 0
}

        for item in db["invalid_items"]:
            erros = item["errors"]

            if len(erros) > 1:
                motivos["Múltiplos erros"] += 1
            else:
                erro = erros[0]

                if "peso" in erro.lower():
                    motivos["Peso fora do padrão"] += 1

                elif "cor" in erro.lower():
                    motivos["Cor inválida"] += 1

                elif "tamanho" in erro.lower():
                    motivos["Tamanho incorreto"] += 1
                    
        print("\n=== RELATÓRIO ===")
        print(f"Caixas completas: {total_closed_boxes}")
        print(f"Peças boas: {total_valid}")
        print(f"Peças reprovadas: {total_invalid}")

        print("\nMotivos de reprovação:")
        for motivo, qtd in motivos.items():
            print(f"- {motivo}: {qtd} peças")

        print("=================\n")