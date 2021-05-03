from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

coffee_cookie = ["コーヒークッキー","アップランド小麦粉×1","コーヒービーン×1","ガーデンビートシュガー×1","ファイアクリスタル×7","ウォータークリスタル×7","","",""]
chicken_fettuccine = ["チキンフェットゥチーネ","地鶏のモモ肉×2","フラントーヨオイル×2","ペパーミント×1","カーリーパセリ×1","クリーム×1","ヴァーミセリ×2","ファイアクラスター×3","ウォータークラスター×3"]
smoke_chicken = ["スモークチキン","地鶏のモモ肉×2","フラントーヨオイル×2","リトルレモン×1","ダークペッパー×2","クリームマッシュルーム×1","アラミゴ塩×1","ファイアクラスター×3","ウォータークラスター×3"]

materials = ["","","","","","","","",""]

# トップ画面
@app.route('/')
def index():
    return render_template('index.html',materials=materials)

@app.route("/sendtext", methods=["GET", "POST"])
def send_text():
    name = request.form["example"]
    if name == "コーヒークッキー":
        materials[0] = coffee_cookie[0]
        materials[1] = coffee_cookie[1]
        materials[2] = coffee_cookie[2]
        materials[3] = coffee_cookie[3]
        materials[4] = coffee_cookie[4]
        materials[5] = coffee_cookie[5]
        materials[6] = coffee_cookie[6]
        materials[7] = coffee_cookie[7]
        materials[8] = coffee_cookie[8]
        return render_template('index.html',materials = materials)
    elif name == "チキンフェットチーネ":
        materials[0] = chicken_fettuccine[0]
        materials[1] = chicken_fettuccine[1]
        materials[2] = chicken_fettuccine[2]
        materials[3] = chicken_fettuccine[3]
        materials[4] = chicken_fettuccine[4]
        materials[5] = chicken_fettuccine[5]
        materials[6] = chicken_fettuccine[6]
        materials[7] = chicken_fettuccine[7]
        materials[8] = chicken_fettuccine[8]
        return render_template('index.html',materials = materials)
    elif name == "スモークチキン":
        materials[0] = smoke_chicken[0]
        materials[1] = smoke_chicken[1]
        materials[2] = smoke_chicken[2]
        materials[3] = smoke_chicken[3]
        materials[4] = smoke_chicken[4]
        materials[5] = smoke_chicken[5]
        materials[6] = smoke_chicken[6]
        materials[7] = smoke_chicken[7]
        materials[8] = smoke_chicken[8]
        return render_template('index.html',materials = materials)

# サーバー起動
app.run(debug=False , host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
