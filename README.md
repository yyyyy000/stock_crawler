# stock_crawler
# 股市爬蟲

在金融市場中，股票資訊是投資者和分析師分析和做出明智投資決策的重要依據。然而，手動獲取和整理股票資訊往往耗時且容易出錯。為了解決這個問題，我們可以使用一個自動化的 Python 程式，這個程式能夠快速抓取股票資訊並將其存儲到 Excel 檔案中，大大提升分析效率並節省寶貴的時間。

這個 Python 程式利用了 xml.etree.ElementTree 和 openpyxl 兩個強大的函式庫。它能夠解析 XML 格式的股票資訊，並將其轉換為易於分析的字典格式。接著，程式會自動建立一個 Excel 檔案，並在其中創建工作表以存儲股票資訊。以下是程式的主要功能：
- 抓取股票資訊：
  透過使用者提供的 XML 檔案，程式能夠解析檔案並獲取股票資訊的相關細節，例如起始年份、結束年份、股票代號等。
- 自動化填充：
  程式使用 API 來獲取每天的股票資訊，並自動將這些資訊填充到 Excel 工作表中的指定行和列。這樣，使用者不需要手動複製和貼上資訊，節省了大量的時間和精力。
- 日期範圍生成：
  程式還提供了一個方便的函式，能夠根據使用者提供的起始年份、結束年份、起始月份和結束月份生成一個日期範圍的列表。這有助於自動化抓取特定時間段的股票資訊。
- 儲存資料：
  程式將抓取到的股票資訊存儲到 Excel 檔案中，方便後續的分析和處理。使用者可以自由命名 Excel 檔案，並將資料保存在其中。

這個自動抓取股票資訊的 Python 程式是一個強大的工具，為投資者和分析師提供了一種快速、高效且準確地獲取股票資訊的方法。通過自動化的方式，它大大提升了分析效率，節省了寶貴的時間，同時減少了錯誤的發生，因此您可以不用再長時間的盯著螢幕啦！。使用者可以更專注於股票資訊的分析和評估，從而做出更明智的投資決策。

當然！以下是使用新手友善的口吻來描述如何使用這個自動抓取股票資訊的 Python 程式的步驟：

準備你的股票資訊：

首先，確保你有一個股票資訊的檔案，其中包含你感興趣的股票的相關資訊，比如成交股數、成交金額、開盤價等等。你可以從網路上找到這樣的資訊，然後將它保存為一個文本檔案。
安裝必要的工具：

在你的電腦上安裝 Python 程式語言以及所需的函式庫。這些函式庫是 xml.etree.ElementTree 和 openpyxl。你可以使用簡單的命令來安裝它們，並在命令提示字元或終端機中執行：
Copy code
pip install xml.etree.ElementTree openpyxl
打開程式碼：

打開一個文本編輯器，並將程式碼複製並粘貼到新的檔案中，並將它保存為 stock_info.py 或其他你喜歡的名稱。
設定檔案和參數：

在程式碼的開頭部分，你會看到一行 tree = ET.parse("data.xml")。將 "data.xml" 更改為你剛才準備的股票資訊檔案的路徑。還有其他的參數，如股票代號和 Excel 檔案名稱，你也可以根據你的需要進行修改。
執行程式：

打開命令提示字元或終端機，並導航到存放程式的目錄。然後執行以下命令：
Copy code
python stock_info.py
等待程式執行：

程式開始運行後，它會自動從股票資訊檔案中抓取相關資訊，並將其存儲到 Excel 檔案中。在這個過程中，請耐心等待，不要中途干擾程式的執行。
檢查結果：

程式執行完畢後，你可以在相同的目錄下找到生成的 Excel 檔案，根據你在程式碼中設定的名稱來命名。打開這個 Excel 檔案，你將看到抓取到的股票資訊。
恭喜！你已經成功地使用這個自動抓取股票資訊的 Python 程式了。你可以通過查看 Excel 檔案中的資料，進一步分析這些股票資訊，並進行其他相關的操作和報告。

重要提示：在使用這個程式之前，請確保你有合法的授權來獲取和使用股票資訊。同時，請遵守相關的法律和規定，以確保合法且合規的使用。
