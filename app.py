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

@app.route('/taste')
def taste():
    """味わい診断ページ"""
    # URLパラメータ type を受け取る(例: ?type=芋焼酎)
    drink_type = request.args.get('type', '')
    return render_template('taste.html')

# PythonAnywhere用の設定
# PythonAnywhereではこの部分は不要だが、ローカルでテストする場合に便利
if __name__ == '__main__':
    app.run(debug=True)
