# NUCT WAL auto connector 勤益科大網路連接腳本

國立勤益科技大學，全自動連接網路腳本，開源程式碼，沒有任何技術專利，安心使用。  


## 開發環境

- Windows Home 11
- Python 3.7.0
- selenium 3.0
- urllib3 1.26.6


## 如何執行

步驟 一：使用 `selenium` 視覺化爬蟲模組（使用版本 `3.0`）。  

```bash
pip install selenium==4.6.0
```

步驟 二：安裝相依模組。  

```bash
pip install requests
```

步驟 三：`ssl` 的版本與 `urllib3` 不相容，[參見議題](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu)。  

```bash
pip install urllib3==1.26.6
```

步驟 三：下載你所要開啟登入頁面的瀏覽器（推薦用你常用的瀏覽器，**驅動版本要與瀏覽器版本相符**）。

| 版本 | 描述 |
| ---- | ---- |
| Chrome | https://chromedriver.chromium.org/downloads |
| Firefox | https://github.com/mozilla/geckodriver/releases |
  
步驟 四：點擊 `auto-reconnect.py` 去啟動腳本。

大功告成！它會自動執行，當你網路斷線，它會自動重新連線，過程非常快，不會有斷網的感覺，24/7執行。


## 版本差異

| 版本 | 描述 |
| ---- | ---- |
| v1 | 不使用 `selenium` 就可以完成動作，不過礙於不知道如何輸入帳密和送出，因此作罷失敗。 |
| v2 | 使用 `selenium` 完成動作，完善只有必要中文提示詞與排除非預期錯誤。 |
| v3 | 同上，完善完整只有英文提示詞（避免顯示編碼問題）與排除非預期錯誤，增加計時功能與完善非預期狀況。 |
| v4 | 同上，我完善非預期狀況。 |
| v5 | 同上，使用 `Pyinstaller` 打包成 `.exe` |


## 貢獻

都是自己寫的，哈哈，這頗簡單ㄚ。  
可以輸入自己的帳號密碼，或是用學校公用的帳密。


## 著作權

此專案受到 [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.zh-tw.html) 保障。  
Copyright © 2023 zong zong ( zongzong0408 )