import os

css = """/* 統合スタイルシート */

/* ===== 共通スタイル ===== */
* {
  box-sizing: border-box;
}

body {
  font-family: "Hiragino Sans", "Meiryo", sans-serif;
  margin: 0;
  padding: 20px;
}

h1 {
  color: #444;
}

label {
  display: block;
  font-weight: bold;
}

.result {
  margin-top: 20px;
  padding: 20px;
  border-radius: 12px;
  font-weight: bold;
  color: #444;
}

/* ===== index.html用 ===== */
body.index {
  background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.index .container {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  padding: 40px 30px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 500px;
  width: 100%;
}

.index h1 {
  font-size: 1.7em;
  margin-bottom: 35px;
  line-height: 1.4;
}

.choice-btn {
  display: block;
  width: 100%;
  padding: 15px;
  margin: 15px 0;
  background: #fff;
  border: 2px solid #ddd;
  border-radius: 12px;
  font-size: 1.1em;
  cursor: pointer;
  text-decoration: none;
  color: #333;
  transition: all 0.3s;
}

.choice-btn:hover {
  border-color: #66bb6a;
  background: #f6fff6;
  box-shadow: 0 2px 8px rgba(102, 187, 106, 0.3);
}

/* ===== taste.html用 ===== */
body.taste {
  background: linear-gradient(135deg, #a6c1ee, #fbc2eb);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.taste .container {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 30px 25px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 420px;
  width: 100%;
}

.taste h1 {
  font-size: 1.5em;
  margin-bottom: 20px;
}

.question {
  margin: 20px 0;
  text-align: left;
}

.question label {
  margin-bottom: 8px;
}

.slider {
  width: 100%;
  margin: 10px 0 5px;
}

.ticks {
  display: flex;
  justify-content: space-between;
  font-size: 0.8em;
  color: #777;
  margin-top: 4px;
  margin-bottom: 10px;
}

.ticks span {
  flex: 0 0 auto;
  text-align: center;
  width: 0;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
}

.value {
  font-size: 0.9em;
  color: #666;
  text-align: right;
}

.btn {
  display: block;
  width: 100%;
  padding: 14px;
  margin: 18px 0 8px;
  background: #fff;
  border: 2px solid #ddd;
  border-radius: 12px;
  font-size: 1.05em;
  cursor: pointer;
  text-decoration: none;
  color: #333;
  transition: all 0.3s;
}

.btn:hover {
  border-color: #42a5f5;
  background: #f0faff;
  box-shadow: 0 2px 8px rgba(66, 165, 245, 0.3);
}

.taste .result {
  margin-top: 15px;
}

.result-card {
  background: #f8fbff;
  border: 1px solid #e0ecff;
  border-radius: 14px;
  padding: 16px;
  box-shadow: 0 4px 12px rgba(66, 165, 245, 0.12);
}

.result-main {
  display: flex;
  gap: 14px;
  align-items: center;
  justify-content: space-between;
}

.result-text {
  flex: 1;
  text-align: left;
}

.result-title {
  font-size: 0.95em;
  color: #3b5fc0;
  margin-bottom: 4px;
}

.result-name {
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 10px;
}

.result-info {
  list-style: none;
  padding: 0;
  margin: 0;
  color: #555;
  font-weight: normal;
  line-height: 1.5;
}

.result-img-wrap {
  width: 120px;
  min-width: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-image {
  max-width: 100%;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
  background: #fff;
}

/* ===== osake.html用 ===== */
body.osake {
  background: #f9f9f9;
}

.osake h1 {
  text-align: center;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.section label {
  margin-top: 10px;
}

.osake .result {
  background: #e6ffe6;
  border: 2px solid #66bb6a;
  font-size: 1.2em;
}
"""

path = 'static/style.css'
with open(path, 'w', encoding='utf-8') as f:
    f.write(css)
print(f'✓ {path} を復旧しました')
