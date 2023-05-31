from abc import ABC, abstracmethod

from database import DatabaseMangager


class PersistenceLayer(ABC):
    @abstracmethod
    def create(self, data):
        raise NotImplementedError("Persistence layers must implement a create method")

    @abstracmethod
    def list(self, order_by=None):
        raise NotImplementedError("Persistence layers must implement a list method")

    @abstracmethod
    def edit(self, bookmark_id, bookmark_data):
        raise NotImplementedError("Persistence layers must implement a edit method")

    @abstracmethod
    def delete(self, bookmark_id):
        raise NotImplementedError("Persistence layers must implement a delete method")


class BookmarkDatabase(PersistenceLayer):
    def __init__(self):
        self.table_name = "bookmarks"
        self.db = DatabaseMangager("bookmarks.db")

        self.db.create_table("bookmarks", {
            "ID": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "TITLE": "TEXT NOT NULL",
            "URL": "TEXT NOT NULL",
            "NOTES": "TEXT",
            "DATE_ADDED": "TEXT NOT NULL",
        })

    def create(self, bookmark_data):
        self.db.add(self.table_name, bookmark_data)

    def list(self, order_by=None):
        return self.db.select(self.table_name, order_by=order_by).fetchall()

    def edit(self, bookmark_id, bookmark_data):
        self.db.update(self.table_name, {"id": bookmark_id}, bookmark_data)

    def delete(self, bookmark_id):
        self.db.delete(self.table_name, {"id": bookmark_id})
