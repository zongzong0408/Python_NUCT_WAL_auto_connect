# NUCT WAL auto connector 勤益科大網路連接腳本

國立勤益科技大學，全自動連接網路腳本，開源程式碼，沒有任何技術專利，安心使用。  

## 開發環境

- Windows Home 11
- Python 3.7.0

## 如何執行

使用 `selenium` 視覺化爬蟲模組。  

```bash
pip install selenium
```

點擊 `auto-reconnect.py` 去啟動腳本。  

## 版本差異

| 版本 | 描述 |
| ---- | ---- |
| v1 | 不想用 `selenium` 就可以完成動作，不過礙於不知道如何輸入帳密和送出，因此作罷失敗。 |
| v2 | 使用 `selenium` 完成動作，完善只有必要中文提示詞與排除非預期錯誤。 |
| v2 | 使用 `selenium` 完成動作，完善只有完整英文提示詞與排除非預期錯誤。 |