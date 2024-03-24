#!/usr/bin/python3
"""Initialize the models directory"""

from models.engine.file_storage import FileStorage

# Initialize FileStorage instance for data storage
storage = FileStorage()

# Load previously stored data (if any)
try:
    storage.reload()
except Exception as e:
    print("Error occurred while reloading storage:", e)
