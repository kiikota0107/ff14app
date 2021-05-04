from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

coffee_cookie = ["コーヒークッキー","アップランド小麦粉","コーヒービーン","ガーデンビートシュガー","ファイアクリスタル","ウォータークリスタル","","",""]
chicken_fettuccine = ["チキンフェットゥチーネ","地鶏のモモ肉","フラントーヨオイル","ペパーミント","カーリーパセリ","クリーム","ヴァーミセリ","ファイアクラスター","ウォータークラスター"]
smoke_chicken = ["スモークチキン","地鶏のモモ肉","フラントーヨオイル","リトルレモン","ダークペッパー","クリームマッシュルーム","アラミゴ塩","ファイアクラスター","ウォータークラスター"]

materials = ["","","","","","","","",""]

# トップ画面
@app.route('/')
def index():
    return render_template('index.html',materials = materials)

@app.route("/sendtext", methods=["GET", "POST"])
def send_text():
    name = request.form["example"]
    num = int(request.form["input_num"])
    if name == "コーヒークッキー":
        materials[0] = coffee_cookie[0] + "×" + str(num*3)
        materials[1] = coffee_cookie[1] + "×" + str(num)
        materials[2] = coffee_cookie[2] + "×" + str(num)
        materials[3] = coffee_cookie[3] + "×" + str(num*7)
        materials[4] = coffee_cookie[4] + "×" + str(num*7)
        materials[5] = coffee_cookie[5]
        materials[6] = coffee_cookie[6]
        materials[7] = coffee_cookie[7]
        materials[8] = coffee_cookie[8]
        return render_template('index.html',materials = materials)
    elif name == "チキンフェットチーネ":
        materials[0] = chicken_fettuccine[0] + "×" + str(num*3)
        materials[1] = chicken_fettuccine[1] + "×" + str(num*2)
        materials[3] = chicken_fettuccine[3] + "×" + str(num*2)
        materials[2] = chicken_fettuccine[2] + "×" + str(num)
        materials[4] = chicken_fettuccine[4] + "×" + str(num)
        materials[5] = chicken_fettuccine[5] + "×" + str(num)
        materials[6] = chicken_fettuccine[6] + "×" + str(num*2)
        materials[7] = chicken_fettuccine[7] + "×" + str(num*3)
        materials[8] = chicken_fettuccine[8] + "×" + str(num*3)
        return render_template('index.html',materials = materials)
    elif name == "スモークチキン":
        materials[0] = smoke_chicken[0] + "×" + str(num*3)
        materials[1] = smoke_chicken[1] + "×" + str(num*2)
        materials[2] = smoke_chicken[2] + "×" + str(num*2)
        materials[3] = smoke_chicken[3] + "×" + str(num)
        materials[4] = smoke_chicken[4] + "×" + str(num*2)
        materials[5] = smoke_chicken[5] + "×" + str(num)
        materials[6] = smoke_chicken[6] + "×" + str(num)
        materials[7] = smoke_chicken[7] + "×" + str(num*3)
        materials[8] = smoke_chicken[8] + "×" + str(num*3)
        return render_template('index.html',materials = materials)

# サーバー起動
app.run(debug=False , host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
