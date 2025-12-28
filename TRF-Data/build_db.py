cd ~/Desktop/tushare_test
cat > build_db.py << 'PY'
import os
import pandas as pd
import akshare as ak

# ===== 股票数据库（qfq，前复权）=====
WATCHLIST = [
    ("002371", "北方华创"),
    ("301286", "侨源股份"),
    ("000066", "中国长城"),
    ("300274", "阳光电源"),
    ("603123", "翠微股份"),
    ("600111", "北方稀土"),
    ("688568", "中科星图"),
    ("688120", "华海清科"),
    ("300236", "上海新阳"),
    ("300593", "新雷能"),
    ("600118", "中国卫星"),
    ("688048", "长光华芯"),
]

START_DATE = "20160101"
OUT_DIR = "db"
os.makedirs(OUT_DIR, exist_ok=True)

def fetch_qfq(symbol: str, start_date: str) -> pd.DataFrame:
    df = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date=start_date,
        adjust="qfq"
    )
    df.rename(columns={
        "日期": "trade_date",
        "开盘": "open",
        "收盘": "close",
        "最高": "high",
        "最低": "low",
        "成交量": "vol",
        "成交额": "amount",
    }, inplace=True)

    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.strftime("%Y%m%d")

    # ===== 均线体系（你已定型）=====
    df["MA20"]  = df["close"].rolling(20).mean()
    df["MA60"]  = df["close"].rolling(60).mean()
    df["MA120"] = df["close"].rolling(120).mean()
    df["MA250"] = df["close"].rolling(250).mean()

    return df

def main():
    ok, fail = 0, 0
    for code, name in WATCHLIST:
        try:
            df = fetch_qfq(code, START_DATE)
            out = os.path.join(OUT_DIR, f"{code}_{name}.csv")
            df.to_csv(out, index=False, encoding="utf-8-sig")
            print(f"✅ {code} {name} | rows={len(df)}")
            ok += 1
        except Exception as e:
            print(f"❌ {code} {name} | ERROR: {e}")
            fail += 1

    print(f"\n完成：成功 {ok} / 失败 {fail}，数据库目录：{OUT_DIR}/")

if __name__ == "__main__":
    main()
PY
