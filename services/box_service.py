from services.data_base_service import DataBaseService
from models.storage_box import StorageBox
from utils.id_generator import generate_id

class BoxService(DataBaseService):  

    def generate_batch(self, boxes):
        if not boxes:
            return "BX-001"

        last_batch = max(
            int(box["batch_number"].split("-")[1])
            for box in boxes
        )

        next_batch = last_batch + 1

        return f"BX-{next_batch:03d}" 

    def add_item(self, item):
        """Adiciona uma peça a uma caixa disponível.
        Se não houver espaço, cria automaticamente uma nova caixa."""
        db = self._get_db()
        
        item_id = item["id"]

        for i, box in enumerate(db["storage_boxes"]):
            box_obj = StorageBox(**box)

            if box_obj.has_space():
                box_obj.item_ids.append(item_id)

                # fecha automaticamente ao atingir a capacidade máxima
                if box_obj.current_count() >= StorageBox.MAX_ITEMS:
                    box_obj.is_closed = True

                db["storage_boxes"][i] = box_obj.to_dict()
                self._save_db(db)

                return box_obj

        new_box = StorageBox(
            id = generate_id("box_id"),
            batch_number=self.generate_batch(db["storage_boxes"]),
            item_ids=[item_id],
            is_closed=False
        )
    
        db["storage_boxes"].append(new_box.to_dict())
    
        self._save_db(db)
    
        return new_box
    
    def list_boxes(self):
        db = self._get_db()
        for box in db["storage_boxes"]:
            print(
                f'ID: {box["id"]} | '
                f'Batch: {box["batch_number"]} | '
                f'Itens: {len(box["item_ids"])} | '
                f'Fechada: {box["is_closed"]}'
            )

    def list_closed_boxes(self):
        db = self._get_db()
        for box in db["storage_boxes"]:
            if box["is_closed"]:
                print(
                    f'ID: {box["id"]} | '
                    f'Batch: {box["batch_number"]} | '
                    f'Itens: {len(box["item_ids"])}'
                )

    def show_box_items(self):

        db = self._get_db()

        box_id = int(input("Informe o id da caixa para listar os itens:  "))

        selected_box = None
        for box in db["storage_boxes"]:
            if box["id"] == box_id:
                selected_box = box
                break

        if not selected_box:
            print("Caixa não encontrada")
            return

        print(f"\nItens da caixa {selected_box['batch_number']}:")

        for item_id in selected_box["item_ids"]:
            item = next(
                (item for item in db["items"] if item["id"] == item_id),
                None
            )

            if item:
                print(
                    f'ID: {item["id"]} | '
                    f'Peso: {item.get("weight_g")} | '
                    f'Cor: {item.get("color")} | '
                    f'Tamanho: {item.get("length_cm")}'
                )