from services.data_base_service import DataBaseService
from models.item import Item
from models.storage_box import StorageBox
from services.box_service import BoxService
from utils.id_generator import generate_id

class ItemService(DataBaseService):

    def store_part(self, weight_g, color, length_cm):
        """Registra uma peça no sistema.
        Valida os dados antes de gerar ID. Caso inválida,
        armazena em invalid_items. Caso válida, salva e envia
        para o serviço de caixas."""

        # valida antes de gerar ID para evitar "buracos" na sequência
        temp_item = Item(None, weight_g, color, length_cm)
        errors = temp_item.validation()

        if errors:
            invalid_id = generate_id("invalid_item_id")

            invalid = {
                "id": invalid_id,
                "weight_g": weight_g,
                "color": color,
                "length_cm": length_cm,
                "errors": errors
            }

            db = self._get_db()
            db["invalid_items"].append(invalid)

            self._save_db(db)

            print(errors)
            return None

        item_id = generate_id("item_id")

        item = Item(item_id, weight_g, color, length_cm)

        db = self._get_db()
        db["items"].append(item.__dict__)

        self._save_db(db)

        BoxService().add_item(item.__dict__)
        print("Peça registrada")

    def list_items(self):
        db = self._get_db()
        for item in db["items"]:
            print(f'ID: {item["id"]} | Peso: {item["weight_g"]}g | Cor: {item["color"]} | Tamanho: {item["length_cm"]}cm')

    def list_invalid_items(self):
        db = self._get_db()
        for item in db["invalid_items"]:
           print(f'ID: {item["id"]} | Peso: {item["weight_g"]}g | Cor: {item["color"]} | Tamanho: {item["length_cm"]}cm')
    
    def delete_item(self):

        db = self._get_db()

        for item in db["items"]:
            print(f'ID: {item["id"]}')

        item_id = int(input("Digite o ID da peça para excluir: "))

        if not any(item["id"] == item_id for item in db["items"]):
            print("Item não encontrado")
            return

        db["items"] = [item for item in db["items"] if item["id"] != item_id]

        for i, box in enumerate(db["storage_boxes"]):
            box_obj = StorageBox(**box)

            if item_id in box_obj.item_ids:
                box_obj.item_ids.remove(item_id)

                # reabre a caixa caso tenha sido fechada anteriormente
                if box_obj.is_closed:
                    box_obj.is_closed = False

                db["storage_boxes"][i] = box_obj.to_dict()

        self._save_db(db)

        print(f"Item {item_id} excluído com sucesso!")