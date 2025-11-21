import sqlite3

conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()



cursor.execute("""

CREATE TABLE IF NOT EXISTS recipes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    ingredients TEXT
)
""")

cursor.execute("INSERT INTO recipes (title, ingredients) VALUES (?, ?)",
               ("Борщ", "свекла, капуста, мясо"))




cursor.execute("SELECT * FROM recipes")

print("Все рецепты:", cursor.fetchall())

cursor.execute("UPDATE recipes SET title=? WHERE id=1",
               ("Красный борщ",))


cursor.execute("DELETE FROM recipes WHERE id=1")

conn.commit()
conn.close()