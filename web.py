from flask import Flask,render_template,jsonify
from flask import request,redirect
import sqlite3
from clv import getCLVA,getRFMA,visualize_rfmA,getCLVB,getRFMB,visualize_rfmB,getCLVC,getRFMC,visualize_rfmC

app = Flask(__name__, static_folder='static')


#首頁(分店飲品總銷售數據)
@app.route("/")
def getindex():    
    return render_template("index.html")

#分店飲品總銷售數據
@app.route("/get/detail")
def get_detail():
    return render_template("index.html")

#月銷售量總額數據
@app.route("/get/month")
def get_month():
    return render_template("sales/monthales.html")

#分店月銷售量總額數據
@app.route("/get/month2")
def get_month2():
    return render_template("sales/monthsales2.html")

#季銷售量總額數據
@app.route("/get/season")
def get_season():
    return render_template("sales/seasonsales.html")

#分店季銷售量總額數據
@app.route("/get/season2")
def get_season2():
    return render_template("sales/seasonsales2.html")



#會員管理(分頁問題待改)
@app.route("/get/member")
def get_member():
    return render_template('clv/member.html')

#分店數據
# df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSRJAYjbzy0TdmOKPD6Q_ubs9gn1W2iGgSUeyhi81FlBNtyaJvrSIwapi1sxOAb-GCCuvXoElDXzQ70/pub?output=csv')
# df2 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT6Ym-aRhDhofx9qPDW9LOC-0fVfWUUZ9ObZsCjW675k2C6iJdAHe3uPdsHiFtn7k36xuRx5vRCOX9J/pub?output=csv')
# df3 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRhlswRtM56BMVFrp11ogd1x02wgXO-oFVWp_bdmUyto1u27pTM757L8SNKT1PR0_ES_zh1Tc-XsE5x/pub?output=csv')

#分店A
@app.route("/get/clvA")
def get_clvA():
    rfm = getRFMA()
    clv_df = getCLVA()
    img_dataA = visualize_rfmA(rfm)
    return render_template('clv/clv.html', clv_df=clv_df, img_dataA=img_dataA)
#分店B
@app.route("/get/clvB")
def get_clvB():
    rfm = getRFMB()
    clv_df = getCLVB()
    img_dataB = visualize_rfmB(rfm)
    return render_template('clv/clv2.html', clv_df=clv_df,img_dataB=img_dataB)
#分店C
@app.route("/get/clvC")
def get_clvC():
    rfm = getRFMC()
    clv_df = getCLVC()
    img_dataC = visualize_rfmC(rfm)
    return render_template('clv/clv3.html', clv_df=clv_df, img_dataC=img_dataC)


#分店A庫存量與進貨
@app.route('/showIngredient1')
def show_Ingredient1():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()

    # 查询store1的資料
    cursor.execute("SELECT * FROM store1")
    data_store1 = cursor.fetchall()

    conn.close()
    return render_template('ingredient/Ingredientstore1.html', data_store1=data_store1)
#add
@app.route("/addIngredient1",methods=["POST"])
def addIngredient1():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()
    addquantity = float(request.form["addquantity"])
    ing_id=float(request.form["ing_id"])

    # 獲取原始數量
    c = cursor.execute("SELECT Quantity FROM store1 WHERE Ing_ID= ?",(ing_id,))
    current_quantity = float(c.fetchone()[0])

    # 計算新的數量
    new_quantity = current_quantity + addquantity

    # 更新table
    cursor.execute("UPDATE store1 SET Quantity = ? WHERE Ing_ID= ?", (new_quantity,ing_id,))
    conn.commit()
    return redirect("/showIngredient1")

#分店A畫圖
@app.route('/api/showIngredient1')
def api_show_Ingredient1():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM store1")
    data_store1 = cursor.fetchall()

    conn.close()
    return jsonify(data_store1)

#分店B庫存量與進貨
@app.route('/showIngredient2')
def show_Ingredient2():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()

    # 查询store1的資料
    cursor.execute("SELECT * FROM store2")
    data_store2 = cursor.fetchall()

    conn.close()
    return render_template('ingredient/Ingredientstore2.html', data_store2=data_store2)
#add
@app.route("/addIngredient2",methods=["POST"])
def addIngredient2():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()
    addquantity = float(request.form["addquantity"])
    ing_id=float(request.form["ing_id"])

    # 獲取原始數量
    c = cursor.execute("SELECT Quantity FROM store2 WHERE Ing_ID= ?",(ing_id,))
    current_quantity = float(c.fetchone()[0])

    # 計算新的數量
    new_quantity = current_quantity + addquantity

    # 更新table
    cursor.execute("UPDATE store2 SET Quantity = ? WHERE Ing_ID= ?", (new_quantity,ing_id,))
    conn.commit()
    return redirect("/showIngredient2")

#分店B畫圖
@app.route('/api/showIngredient2')
def api_show_Ingredient2():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM store2")
    data_store2 = cursor.fetchall()

    conn.close()
    return jsonify(data_store2)

#分店C原料庫存與進貨
@app.route('/showIngredient3')
def show_Ingredient3():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()

    # 查询store1的資料
    cursor.execute("SELECT * FROM store3")
    data_store3 = cursor.fetchall()

    conn.close()
    return render_template('ingredient/Ingredientstore3.html', data_store3=data_store3)
#add
@app.route("/addIngredient3",methods=["POST"])
def addIngredient3():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()
    addquantity = float(request.form["addquantity"])
    ing_id=float(request.form["ing_id"])

    # 獲取原始數量
    c = cursor.execute("SELECT Quantity FROM store3 WHERE Ing_ID= ?",(ing_id,))
    current_quantity = float(c.fetchone()[0])

    # 計算新的數量
    new_quantity = current_quantity + addquantity

    # 更新table
    cursor.execute("UPDATE store3 SET Quantity = ? WHERE Ing_ID= ?", (new_quantity,ing_id,))
    conn.commit()
    return redirect("/showIngredient3")

#分店C畫圖
@app.route('/api/showIngredient3')
def api_show_Ingredient3():
    conn = sqlite3.connect('Ingredient.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM store3")
    data_store3 = cursor.fetchall()

    conn.close()
    return jsonify(data_store3)

#預測分店A
@app.route("/forecastA")
def forcastA():
    return render_template("/forecast/store1Forecast.html")

#預測分店B
@app.route("/forecastB")
def forcastB():
    return render_template("/forecast/store2Forecast.html")

#預測分店C
@app.route("/forecastC")
def forcastC():
    return render_template("/forecast/store3Forecast.html")


@app.route("/get/chart")
def get_chart():
    return render_template("get_chart.html")



if __name__ == '__main__':
    app.run()