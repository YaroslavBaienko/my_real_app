import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS lists (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")
db.commit()

while True:
    user_login = input("Login: ")
    user_password = input("Password: ")
    if user_login == "" or user_password == "":
        print("Нельзя вводить пустое значение")
        continue

    # sql.execute("SELECT login FROM lists")
    # if sql.fetchone() is None:
    sql.execute(f"INSERT INTO lists VALUES (?, ?, ?)", (user_login, user_password, 0))
    db.commit()
    # else:
    #     print("Такая запись уже имеется")
