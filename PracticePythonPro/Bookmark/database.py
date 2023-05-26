import sqlite3


class DatabaseMangager:
    def __init__(self, db_name,):
        self.connection = sqlite3.connect(db_name)

    def __del__(self):
        self.connection.close()

    def _execute(self, statement, values=None):
        with self.connection:  # Data transaction
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name, columns):
        column_and_datatype = [f"{column_name} {d_type}" for column_name, d_type in columns.items()]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({",".join(column_and_datatype)});
            """
        )

    def add(self, table_name, columns):
        placeholders = ", ".join("?" * len(columns))
        column_name = ", ".join(columns.keys())
        values = tuple(columns.values())

        self._execute(
            f"""
            INSERT INTO {table_name}
            ({column_name}) VALUES ({placeholders});""",
            values,
        )

    def delete(self, table_name, criteria):
        placeholders = [f"{column} = ?" for column in criteria.keys()]
        delete_criteria = " AND ".join(placeholders)
        self._execute(
            f"""
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            """,
            tuple(criteria.values())
        )

    def select(self, table_name, criteria=None, order_by=None):
        criteria = criteria or {}

        query = f"SELECT * FROM {table_name}"

        if criteria:
            palceholders = [f"{column} = ?" for column in criteria.keys()]
            select_criteria = " AND ".join(palceholders)
            query += f" WHERE {select_criteria}"

        if order_by:
            query += f" ORDER BY {order_by}"

        return self._execute(
            query,
            tuple(criteria.values())
        )

    def update(self, table_name, criteria, data):
        placeholders = [f"{column} = ?" for column in criteria.keys()]
        update_criteria = " AND ".join(placeholders)

        data_placeholders = ", ".join(f"{key} = ?" for key in data.keys())

        values = tuple(data.values()) + tuple(criteria.values())
        self._execute(
            f"""
            UPDATE {table_name}
            SET {data_placeholders}
            WHERE {update_criteria}
            """,
            values,
        )
