from sqlite3 import connect
import shutil
import re

terminal_width, _ = shutil.get_terminal_size()

line = ("-" * terminal_width * 2)[:29:-1]




conn = connect('move.db')
cursor = conn.cursor()

""" ЗАПРОС 1"""

query = "SELECT Title, Cout FROM Materials ORDER BY Cout DESC LIMIT 10"
cursor.execute(query)

results = cursor.fetchall()
print("10 самых дорогих материалов:")
for title, cout in results:
    formatted_title = re.sub(r'\d', '', title).replace("x","").strip()
    print(f"{formatted_title}, С ценой: {int(cout)}")
print(line)

""" ЗАПРОС 2"""
query = "SELECT DISTINCT Title, RATE FROM Supplier WHERE RATE = 99"
cursor.execute(query)

results = cursor.fetchall()
print("Поставщики с рейтингом 99:")
for title, rate in results:
    print(title)
print(line)


""" ЗАПРОС 3"""
query = "SELECT COUNT(*) AS CountOfSuppliers, SUM(RATE) AS TotalRate FROM Supplier"
cursor.execute(query)

results = cursor.fetchall()
for count, total_rate in results:
    print(f"Количество поставщиков: {count}")
    print(f"Сумма рейтингов: {total_rate}")
print(line)

"""Запрос 4"""
query = "SELECT DISTINCT Title, RATE FROM Supplier WHERE RATE > 80"
cursor.execute(query)

results = cursor.fetchall()
print("Поставщики с рейтингом выше 80:")
for title, rate in results:
    print(f"{title} - {rate}")
print(line)



conn.close()
