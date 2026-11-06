from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """ホームページ - ランディング"""
    return render_template('index.html')

@app.route('/select')
def select():
    """種類選択ページ"""
    return render_template('select.html')

# ↓ ここに追加します（容量選択ページへのルーティング）
@app.route('/volume')
def volume():
    """容量選択ページ"""
    drink_type = request.args.get('type', '')
    return render_template('volume.html', drink_type=drink_type)

@app.route('/taste')
def taste():
    """味わい診断ページ"""
    # URLパラメータ type と volume を受け取る
    drink_type = request.args.get('type', '')
    drink_volume = request.args.get('volume', '') # ← ここに volume の受け取りを追加
    return render_template('taste.html', drink_type=drink_type, drink_volume=drink_volume)

@app.route('/result')
def result():
    """診断結果ページ"""
    # 1. 画面から送られてきた条件（種類、容量など）を取得
    selected_type = request.args.get('type', '')
    selected_volume = request.args.get('volume', 'any')

    # 2. 全お酒データを準備（JSONなどから読み込み）
    filtered_drinks = drinks_data 

    # 3. 種類（芋焼酎など）で絞り込み
    if selected_type:
        filtered_drinks = [d for d in filtered_drinks if d.get('種類') == selected_type]

    # ★★★ ここに先ほどの容量絞り込みコードが入ります ★★★
    if selected_volume and selected_volume != 'any':
        if selected_volume == '100':
            filtered_drinks = [d for d in filtered_drinks if int(d.get('volume_ml', 0)) <= 360]
        elif selected_volume == '720':
            filtered_drinks = [d for d in filtered_drinks if 500 <= int(d.get('volume_ml', 0)) <= 900]
        elif selected_volume == '1800':
            filtered_drinks = [d for d in filtered_drinks if int(d.get('volume_ml', 0)) >= 1800]
    # ★★★★★★★★★★★★★★★★★★★★★★★★★★★

    # 4. 絞り込んだ結果を result.html に渡して表示
    return render_template('result.html', drinks=filtered_drinks)

# PythonAnywhere用の設定
if __name__ == '__main__':
    app.run(debug=True)
