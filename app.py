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
    return render_template('taste.html')

# PythonAnywhere用の設定
if __name__ == '__main__':
    app.run(debug=True)
