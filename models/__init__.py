# models/__init__.py

from models.engine.file_storage import FileStorage

storage_engine = FileStorage()

try:
        storage_engine.reload()
except Exception as e:
        print("Error occurred while reloading storage engine:", e)

