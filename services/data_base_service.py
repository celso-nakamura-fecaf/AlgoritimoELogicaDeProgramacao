from db.database import load_db, save_db

class DataBaseService:
    """Classe base para acesso ao banco de dados.
    Centraliza operações de leitura e escrita."""
    def _get_db(self):
        return load_db()

    def _save_db(self, db):
        save_db(db)