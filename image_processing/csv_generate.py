import pandas as pd

# original data
data = """
1101 臺灣水泥
1102 亞洲水泥
1216 統一企業
1301 臺塑企業
1303 南亞塑膠
1326 臺灣化學纖維
1402 遠東新世紀
2002 中國鋼鐵
2105 正新橡膠
2201 裕隆
2207 和泰汽車
2227 裕日車
2301 光寶科技
2303 聯華電子
2308 臺達電子
2317 鴻海精密
2327 國巨
2330 臺灣積體電路製造
2354 鴻準
2357 華碩
2382 廣達電腦
2408 南亞科技
2409 友達光電
2412 中華電信
2474 可成科技
2454 聯發科技
2609 陽明海運
2615 萬海航運
2633 臺灣高鐵
2801 彰化銀行
2880 華南金融控股
2881 富邦金融控股
2882 國泰金融控股
2883 中華開發金融控股
2884 玉山金融控股
2885 元大金融控股
2886 兆豐金融控股
2887 臺新金融控股
2888 新光金融控股
2890 永豐金融控股
2891 中國信託金融控股
2892 第一金融控股
2912 統一超商
3008 大立光電
3045 臺灣大哥大
3481 群創光電
3711 日月光半導體
4904 遠傳電信
4938 和碩
5871 中租控股
5880 合作金庫金融控股
6415 矽力傑
6505 臺塑石化
6669 緯穎科技
6770 力積電
8454 富邦媒體科技
9904 寶成
9910 豐泰企業
"""

lines = data.strip().split('\n')
parsed_data = []
for line in lines:
    parts = line.split()
    company_id = parts[0]
    company_name = ' '.join(parts[1:])
    parsed_data.append([company_id, company_name])

df = pd.DataFrame(parsed_data, columns=['ticker', 'name'])

csv_file = 'data/companies.csv'
df.to_csv(csv_file, index=False, encoding='utf-8-sig')

print(f"complete, filepath: {csv_file}")