# おすすめ焼酎診断アプリ

FlaskベースのWebアプリケーションです。ユーザーの好みに基づいて最適な焼酎を診断します。

## ローカルでの実行方法

```bash
# 仮想環境の作成(推奨)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 依存パッケージのインストール
pip install -r requirements.txt

# アプリの実行
python app.py
```

ブラウザで `http://127.0.0.1:5000/` にアクセスします。

## PythonAnywhereでのデプロイ方法

### 1. PythonAnywhereにログイン
- https://www.pythonanywhere.com/ でアカウントを作成・ログイン

### 2. ファイルのアップロード
**方法A: Webインターフェースから**
- 「Files」タブを開く
- `/home/yourusername/` ディレクトリに `mysite` などのフォルダを作成
- 以下のファイルをアップロード:
  - `app.py`
  - `requirements.txt`
  - `templates/` フォルダと中身のHTMLファイル

**方法B: Gitから(推奨)**
```bash
# Bashコンソールで実行
cd ~
git clone https://github.com/yourusername/yourrepo.git mysite
cd mysite
```

### 3. 仮想環境の作成とパッケージインストール
PythonAnywhereの「Bash」コンソールで:
```bash
cd ~/mysite  # プロジェクトディレクトリに移動
python3.10 -m venv venv  # 仮想環境作成(Python3.10を推奨)
source venv/bin/activate  # 仮想環境を有効化
pip install -r requirements.txt  # パッケージインストール
```

### 4. Webアプリの設定
- 「Web」タブを開く
- 「Add a new web app」をクリック
- Pythonバージョンを選択(例: Python 3.10)
- 「Manual configuration」を選択(Flaskを選択しない)

### 5. WSGIファイルの編集
「Web」タブの「Code」セクションで、WSGI configuration fileのリンクをクリックし、以下の内容に置き換え:

```python
import sys
import os

# プロジェクトのパスを追加
path = '/home/yourusername/mysite'  # yourUsernameを実際のユーザー名に変更
if path not in sys.path:
    sys.path.insert(0, path)

# 仮想環境を有効化
activate_this = '/home/yourusername/mysite/venv/bin/activate_this.py'  # yourUsernameを変更
# exec(open(activate_this).read(), {'__file__': activate_this})

# Flaskアプリをインポート
from app import app as application
```

### 6. 仮想環境のパス設定
「Web」タブの「Virtualenv」セクションで:
```
/home/yourusername/mysite/venv
```
と入力(yourusernameは実際のユーザー名)

### 7. リロード
「Web」タブの上部にある緑色の「Reload yourusername.pythonanywhere.com」ボタンをクリック

### 8. アクセス
`https://yourusername.pythonanywhere.com/` にブラウザでアクセス

## トラブルシューティング

### エラーログの確認
- 「Web」タブの「Log files」セクションでエラーログを確認
- Server log、Error logをチェック

### よくある問題
1. **ImportError: No module named 'flask'**
   - 仮想環境が正しく設定されていない
   - 仮想環境内で `pip install -r requirements.txt` を実行したか確認

2. **404 Not Found**
   - WSGIファイルのパス設定を確認
   - `app.py` の場所が正しいか確認

3. **Internal Server Error**
   - Error logを確認
   - パーミッションの問題がないか確認

## ファイル構成

```
mysite/
├── app.py              # Flaskアプリケーション本体
├── requirements.txt    # 依存パッケージリスト
├── README.md          # このファイル
└── templates/         # HTMLテンプレート
    ├── index.html     # トップページ(種類選択)
    ├── osake.html     # お酒診断ページ
    └── taste.html     # 味わい診断ページ
```

## 機能説明

1. **トップページ** (`/`)
   - 芋焼酎、麦焼酎、デーツ焼酎、リキュールから選択

2. **味わい診断** (`/taste?type=芋焼酎`)
   - 香り、味わい、あと味の3つのパラメータをスライダーで調整
   - ユークリッド距離で最も近い銘柄を推薦

3. **お酒診断** (`/osake`)
   - より詳細な診断ページ(オプション)
