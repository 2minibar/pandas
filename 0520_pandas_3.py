import pandas as pd

# ==========================================
# 1. 讀取資料
# ==========================================
# 讀取 CSV 檔案
df = pd.read_csv('SuperMarket Analysis.csv')

print("--- 1. 資料讀取成功，前三筆資料如下 ---")
print(df.head(3))
print("\n" + "="*50 + "\n")


# ==========================================
# 2. 基本統計：總銷售額與平均評分
# ==========================================
total_sales = df['Sales'].sum()
average_rating = df['Rating'].mean()

print("--- 2. 基本統計結果 ---")
print(f"💰 總銷售額 (Total Sales): ${total_sales:,.2f}")
print(f"⭐ 顧客平均評分 (Average Rating): {average_rating:.2f} 分")
print("\n" + "="*50 + "\n")


# ==========================================
# 3. 分組分析 (Groupby)
# ==========================================
# (1) 哪一個城市的總銷售額最高？
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
best_city = city_sales.index[0]
best_city_sales = city_sales.iloc[0]

print("--- 3-1. 各城市銷售額排行 ---")
print(city_sales)
print(f"👉 總銷售額最高的城市是: {best_city} (${best_city_sales:,.2f})")
print("-" * 30)

# (2) 哪一種商品分類的累積銷售數量最多？
product_qty = df.groupby('Product line')['Quantity'].sum().sort_values(ascending=False)
top_product = product_qty.index[0]
top_product_qty = product_qty.iloc[0]

print("--- 3-2. 商品分類銷量排行 ---")
print(product_qty)
print(f"👉 累積銷量最多的商品分類是: {top_product} ({top_product_qty} 件)")
print("\n" + "="*50 + "\n")


# ==========================================
# 4. 資料篩選：會員的消費分析
# ==========================================
# 篩選出 Customer type 為 Member 的資料
member_df = df[df['Customer type'] == 'Member']

# 計算會員的平均消費金額
member_avg_sales = member_df['Sales'].mean()

print("--- 4. 会員資料篩選結果 ---")
print(f"👥 會員總消費筆數: {len(member_df)} 筆")
print(f"💳 會員的平均單筆消費金額: ${member_avg_sales:.2f}")
print("\n" + "="*50 + "\n")


# ==========================================
# 5. 將分析結果匯出（加分項/選做）
# ==========================================
# 把城市銷售排行存成一個新的 CSV 檔
city_sales.to_csv('City_Sales_Report.csv', header=True)
print("🎉 分析完成！各城市報告已匯出為 'City_Sales_Report.csv'")