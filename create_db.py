import sqlite3

conn = sqlite3.connect("projects.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
""")

cursor.execute("""
INSERT INTO projects (title, description)
VALUES
('Portfolio Website', 'Built using Flask and SQLite'),
('AI Mini Project', 'Machine learning project')
""")

conn.commit()
conn.close()

print("Database created successfully")