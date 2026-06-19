with open('static/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old = """.ticks {
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
}"""

new = """.ticks {
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

css = css.replace(old, new)

with open('static/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('CSSを修正しました')
