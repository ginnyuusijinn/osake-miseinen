with open('static/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# ticks のスタイルを修正
old_ticks = """.ticks {
  display: flex;
  justify-content: space-around;
  font-size: 0.8em;
  color: #777;
  margin-top: 4px;
  margin-bottom: 10px;
}

.ticks span {
  flex: 1;
  text-align: center;
  white-space: nowrap;
}"""

new_ticks = """.ticks {
  display: flex;
  justify-content: space-between;
  font-size: 0.75em;
  color: #999;
  margin-top: 2px;
  margin-bottom: 10px;
  padding: 0 1px;
}

.ticks span {
  flex: 0 0 auto;
  text-align: center;
  width: 0;
  transform: translateX(-50%);
}"""

css = css.replace(old_ticks, new_ticks)

with open('static/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('CSSを修正しました - 目盛りをバーの直下に配置')
