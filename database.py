import sqlite3

conn = sqlite3.connect('Ingredient.db')
print("Ingredient Database連接成功")
c = conn.cursor()


#茶葉(克),cost元/1000g
#珍珠(克),cost元/2000g
#冰淇淋(克),cost元/500g
#牛奶(ml),cost元/1000ml
#鮮奶油(ml),cost元/500ml






#table create一次 資料insert一次就可以了 弄完可以先註解掉 

# #第一家分店
# c.execute('''CREATE TABLE store1
#              (Ing_ID INT PRIMARY KEY NOT NULL,
#               Ing_name TEXT NOT NULL,
#               Quantity INT NOT NULL,
#               Cost INT NOT NULL,
#               SafeQuantity INT NOT NULL,
#               Expiration_date TEXT NOT NULL);''')
# print("store1 table建立成功")

# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (1, 'BOPFt茶葉', 2800, 800, 100,'2023-12-08' )")
# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (2, 'GFBOP茶葉', 500, 700, 120,'2023-11-05' )")
# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (3, 'TW茶葉', 200, 300, 50,'2023-11-06' )")
# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (4, '牛奶', 3000, 500, 200,'2023-11-01' )")
# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (5, '珍珠', 2400, 100, 100,'2023-11-18' )")
# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (6, '鮮奶油', 1200, 300, 300,'2023-11-02' )")
# c.execute("INSERT INTO store1 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (7, '冰淇淋', 2200, 200, 100,'2024-02-08' )")
# print("store1 table新增資料成功")

# #第二家分店
# c.execute('''CREATE TABLE store2
#              (Ing_ID INT PRIMARY KEY NOT NULL,
#               Ing_name TEXT NOT NULL,
#               Quantity INT NOT NULL,
#               Cost INT NOT NULL,
#               SafeQuantity INT NOT NULL,
#               Expiration_date TEXT NOT NULL);''')
# print("store2 table建立成功")

# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (1, 'BOPFt茶葉', 1230, 800, 100,'2023-11-07' )")
# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (2, 'GFBOP茶葉', 550, 700, 120,'2023-11-09' )")
# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (3, 'TW茶葉', 120, 300, 50,'2023-11-18' )")
# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (4, '牛奶', 2000, 500, 200,'2023-11-03' )")
# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (5, '珍珠', 240, 100, 100,'2023-11-1' )")
# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (6, '鮮奶油', 1390, 300, 300,'2023-11-02' )")
# c.execute("INSERT INTO store2 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (7, '冰淇淋', 1000, 200, 100,'2024-02-28' )")
# print("store2 table新增資料成功")

# #第三家分店
# c.execute('''CREATE TABLE store3
#              (Ing_ID INT PRIMARY KEY NOT NULL,
#               Ing_name TEXT NOT NULL,
#               Quantity INT NOT NULL,
#               Cost INT NOT NULL,
#               SafeQuantity INT NOT NULL,
#               Expiration_date TEXT NOT NULL);''')
# print("store3 table建立成功")

# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (1, 'BOPFt茶葉', 1600, 800, 100,'2023-11-18' )")
# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (2, 'GFBOP茶葉', 50, 700, 120,'2023-11-01' )")
# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (3, 'TW茶葉', 780, 300, 50,'2023-11-26' )")
# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (4, '牛奶', 300, 500, 200,'2023-11-01' )")
# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (5, '珍珠', 230, 100, 100,'2023-11-12' )")
# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (6, '鮮奶油', 120, 300, 300,'2023-11-02' )")
# c.execute("INSERT INTO store3 (Ing_ID,Ing_name,Quantity,Cost,SafeQuantity,Expiration_date) \
#       VALUES (7, '冰淇淋', 220, 200, 100,'2024-02-18' )")
# print("store3 table新增資料成功")

print("---------------------------------------------")







#查看資料
# 第一家
cursor = c.execute("SELECT Ing_ID, Ing_name, Quantity, Cost, SafeQuantity, Expiration_date FROM store1")
rows = cursor.fetchall()
print("第一家店的原料有:")
for row in rows:
    print("Ing_ID =", row[0])
    print("Ing_name =", row[1])
    print("Quantity =", row[2])
    print("Cost =", row[3])
    print("SafeQuantity =", row[4])
    print("Expiration_date =", row[5], "\n")
print("---------------------------------------------")

# 第二家
cursor = c.execute("SELECT Ing_ID, Ing_name, Quantity, Cost, SafeQuantity, Expiration_date FROM store2")
rows = cursor.fetchall()
print("第二家店的原料有:")
for row in rows:
    print("Ing_ID =", row[0])
    print("Ing_name =", row[1])
    print("Quantity =", row[2])
    print("Cost =", row[3])
    print("SafeQuantity =", row[4])
    print("Expiration_date =", row[5], "\n")
print("---------------------------------------------")

# 第三家
cursor = c.execute("SELECT Ing_ID, Ing_name, Quantity, Cost, SafeQuantity, Expiration_date FROM store3")
rows = cursor.fetchall()
print("第三家店的原料有:",)
for row in rows:
    print("Ing_ID =", row[0])
    print("Ing_name =", row[1])
    print("Quantity =", row[2])
    print("Cost =", row[3])
    print("SafeQuantity =", row[4])
    print("Expiration_date =", row[5], "\n")


conn.commit()
conn.close()
