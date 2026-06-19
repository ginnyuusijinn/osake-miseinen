with open('static/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''.ticks {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  font-size: 0.8em;
  color: #777;
  margin-top: 4px;
  text-align: center;
  gap: 2px;
}'''

new = '''.ticks {
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
}'''

content = content.replace(old, new)

with open('static/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated style.css - ticks now align under slider points')
