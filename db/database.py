import json
import os

DB_FILE = "db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {
            "items": [],
            "storage_boxes": [], 
            "invalid_items": []
            }

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(db):
    """Salva os dados no arquivo JSON de forma segura.
    Utiliza um arquivo temporário e backup para evitar
    corrupção de dados durante a escrita."""

    import json, os, shutil
  
    real_file = "db.json"
    temp_file = "db_temp.json"
    backup_file = "db_backup.json"

    if os.path.exists(real_file):
        shutil.copy(real_file, "db_backup.json")

    with open(temp_file, "w") as f:
       json.dump(db, f, indent=4, ensure_ascii=False)

    os.replace(temp_file, real_file)

    if os.path.exists(backup_file):
        os.remove(backup_file)