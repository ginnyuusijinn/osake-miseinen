import csv
import json
import os

# CSVを読み込む（候補ファイルをすべて処理）
CSV_CANDIDATES = [
    '井上酒造.csv',
    '課題研究おさけ.csv',
    '課題研究おさけ櫻の郷酒造.csv',
]
available_csvs = [candidate for candidate in CSV_CANDIDATES if os.path.exists(candidate)]

if not available_csvs:
    raise FileNotFoundError('入力CSVが見つかりません。候補ファイルを配置してください。')

data = []
for csv_file in available_csvs:
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

# 商品名の正規化（全角スペース→半角スペース）
def normalize_name(name: str) -> str:
    return (name or '').replace('\u3000', ' ').strip()

# 商品ごとのプロファイル（タイプと味わいパラメータ）
profile_map = {
    # 芋焼酎
    '爽 飫肥杉': {'type': '芋焼酎', 'aroma': 5, 'flavor': 5, 'aftertaste': 5},
    '黒飫肥杉': {'type': '芋焼酎', 'aroma': 3, 'flavor': 2, 'aftertaste': 2},

    '赤飫肥杉': {'type': '芋焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 4},
    '飫肥杉 原酒 特選ブレンド': {'type': '芋焼酎', 'aroma': 2, 'flavor': 3, 'aftertaste': 2},
    '飫肥杉 原酒': {'type': '芋焼酎', 'aroma': 2, 'flavor': 3, 'aftertaste': 2},
    '飫肥杉 ライオンズボトル': {'type': '芋焼酎', 'aroma': 5, 'flavor': 5, 'aftertaste': 5},
    '櫻泉': {'type': '芋焼酎', 'aroma': 4, 'flavor': 3, 'aftertaste': 3},
    '大金持 芋 金箔入': {'type': '芋焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 3},
    '芋の達人': {'type': '芋焼酎', 'aroma': 2, 'flavor': 1, 'aftertaste': 2},
    '赤魔性': {'type': '芋焼酎', 'aroma': 4, 'flavor': 2, 'aftertaste': 2},
    '無邪鬼': {'type': '芋焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 3},
    '神武 安納芋仕込長期貯蔵原酒': {'type': '芋焼酎', 'aroma': 2, 'flavor': 1, 'aftertaste': 3},
    '萬甕': {'type': '芋焼酎', 'aroma': 4, 'flavor': 2, 'aftertaste': 3},
    '焼酎力 芋': {'type': '芋焼酎', 'aroma': 4, 'flavor': 2, 'aftertaste': 3},
    'どでか芋': {'type': '芋焼酎', 'aroma': 4, 'flavor': 3, 'aftertaste': 4},

    # 麦焼酎
    '純麦櫻泉': {'type': '麦焼酎', 'aroma': 5, 'flavor': 5, 'aftertaste': 4},
    '黒櫻泉': {'type': '麦焼酎', 'aroma': 1, 'flavor': 2, 'aftertaste': 1},
    '大金持 麦': {'type': '麦焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 3},
    '大金持 麦 金箔入': {'type': '麦焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 3},
    '吉祥大金持': {'type': '麦焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 3},
    '神武　琥珀': {'type': '麦焼酎', 'aroma': 2, 'flavor': 3, 'aftertaste': 2},
    '貴醸酎 神武': {'type': '麦焼酎', 'aroma': 1, 'flavor': 1, 'aftertaste': 2},
    '神武 麦全麹仕込十年貯蔵原酒': {'type': '麦焼酎', 'aroma': 3, 'flavor': 1, 'aftertaste': 3},
    '焼酎力 麦': {'type': '麦焼酎', 'aroma': 5, 'flavor': 4, 'aftertaste': 4},
    'どでか麦': {'type': '麦焼酎', 'aroma': 3, 'flavor': 4, 'aftertaste': 3},

    # リキュール
    '日向の夏子': {'type': 'リキュール', 'aroma': 4, 'flavor': 4, 'aftertaste': 3},
    'さわやか へべすリキュール': {'type': 'リキュール', 'aroma': 4, 'flavor': 3, 'aftertaste': 4},
    'さわやか レモンリキュール': {'type': 'リキュール', 'aroma': 5, 'flavor': 5, 'aftertaste': 4},
    'さわやか ゆずリキュール': {'type': 'リキュール', 'aroma': 5, 'flavor': 4, 'aftertaste': 4},

    # デーツ焼酎
    '孤独な天使': {'type': 'デーツ焼酎', 'aroma': 2, 'flavor': 1, 'aftertaste': 3},
}

# 正規化済みプロフィールマップ
normalized_profile_map = {normalize_name(k): v for k, v in profile_map.items()}


def map_type_label(label: str | None) -> str | None:
    if not label:
        return None
    label = label.strip()
    if label in {'芋焼酎', '麦焼酎', 'リキュール', 'デーツ焼酎', 'その他'}:
        return label
    if label == '芋':
        return '芋焼酎'
    if label == '麦':
        return '麦焼酎'
    if 'デーツ' in label:
        return 'デーツ焼酎'
    if 'リキュール' in label or '梅酒' in label:
        return 'リキュール'
    if 'ジン' in label or 'GIN' in label.upper():
        return 'その他'
    if label == 'その他':
        return 'その他'
    return None

# 価格スコア算出（安い⇔高いを1〜5で表現）
def price_to_score(price):
    if price is None:
        return None
    if price <= 1000:
        return 1
    if price <= 2000:
        return 2
    if price <= 3000:
        return 3
    if price <= 4500:
        return 4
    return 5


def safe_int(value):
    if value is None or str(value).strip() == '':
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def pick_field(row, candidates):
    for key in candidates:
        value = row.get(key)
        if value:
            return value.strip()
    return ''


# 商品名ごとにグループ化して、金額に基づくパラメータを計算
products = {}

def merge_entry(existing, new):
    for field in ('type', 'image', 'link', 'aroma', 'flavor', 'aftertaste'):
        if not existing.get(field) and new.get(field):
            existing[field] = new[field]
    if not existing.get('container') and new.get('container'):
        existing['container'] = new['container']
    if existing.get('price') is None and new.get('price') is not None:
        existing['price'] = new['price']
    if existing.get('abv') is None and new.get('abv') is not None:
        existing['abv'] = new['abv']

for row in data:
    name = normalize_name(row.get('商品名', ''))
    if not name:
        continue
    profile = normalized_profile_map.get(name)
    degree = safe_int(row.get('度数'))
    volume = safe_int(row.get('容量（ml）'))
    price = safe_int(row.get('金額'))
    container = pick_field(row, ['容器', ''])
    image = pick_field(row, ['画像'])
    link = pick_field(row, ['リンク', '商品リンク', 'link'])
    aroma = safe_int(pick_field(row, ['香り'])) or (profile and profile['aroma'])
    flavor = safe_int(pick_field(row, ['味わい'])) or (profile and profile['flavor'])
    aftertaste = safe_int(pick_field(row, ['あと味'])) or (profile and profile['aftertaste'])
    type_label_field = pick_field(row, ['種類', 'type'])
    type_from_label = map_type_label(type_label_field)
    type_value = type_from_label or (profile['type'] if profile else 'その他')

    entry = {
        'name': name,
        'type': type_value,
        'image': image,
        'abv': degree,
        'volume_ml': volume,
        'container': container,
        'price': price,
        'aroma': aroma,
        'flavor': flavor,
        'aftertaste': aftertaste,
        'link': link
    }

    key = (entry['name'], entry['abv'], entry['volume_ml'], entry['price'], entry['container'])
    existing = products.get(key)
    if existing:
        merge_entry(existing, entry)
    else:
        products[key] = entry

expanded_data = []
for entry in products.values():
    expanded = entry.copy()
    expanded['price_score'] = price_to_score(expanded.get('price'))
    expanded_data.append(expanded)

# 拡張CSVを出力
output_file = '拡張_おさけ.csv'
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['name', 'type', 'image', 'abv', 'volume_ml', 'container', 'price', 'aroma', 'flavor', 'aftertaste', 'price_score', 'link']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expanded_data)

print(f"拡張データを生成しました: {output_file}")
print(f"総件数: {len(expanded_data)}")

# JSONでも出力（JavaScriptで使用可能）
static_json = os.path.join('static', 'drinks_data.json')
with open(static_json, 'w', encoding='utf-8') as f:
    json.dump(expanded_data, f, ensure_ascii=False, indent=2)

print(f"JSON形式も生成しました: {static_json}")
