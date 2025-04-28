import yfinance as yf
import pandas as pd

# 定義標的與時間範圍
ticker_symbol = "VOO"
period = "6y"           # 過去五年
interval = "1mo"        # 每月

# 抓取資料
data = yf.download(
    tickers=ticker_symbol,
    period=period,
    interval=interval,
    auto_adjust=False,  # 保留原始收盤價；若想要調整後收盤價，改用 'Adj Close'
    progress=False
)

# 只保留「收盤價」欄位並重新命名
monthly_close = data[["Close"]].rename(columns={"Close": "VOO_Close"})

# 將索引（日期）轉為欄位
monthly_close = monthly_close.reset_index()

# 輸出為 CSV
output_filename = "VOO_monthly_close_6y.csv"
monthly_close.to_csv(output_filename, index=False)

print(f"已將 VOO 近五年每月收盤價儲存至：{output_filename}")
