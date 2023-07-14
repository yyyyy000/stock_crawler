import xml.etree.ElementTree as ET
from openpyxl import Workbook
import requests
import time
#匯入函式庫

def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result

# Print the dictionary
#def print_dict(data):
    for key, value in data.items():
        print(f"{key}: {value}")
def fillsheet(sheet, data, row): 
#建立一個function名稱裡面放置三種參數sheet, data , row
    for column, value in enumerate(data,1):
    #讀取資料
        sheet.cell(row, column = column, value = value)
        #將資料放置在row行column列上，其個子里填寫value資料
def returnStrDayList(startYear, startMonth, endYear, endMonth, day = "01"):
    result = []
    for year in range(startYear, endYear+1):
        if year == startYear:
            for month in range(startMonth, 13):
                month = str(month)
                if len(month) == 1:
                    month = "0" + month
                result.append(str(year)+month+day)
        elif year == endYear:
            for month in range(1, endMonth+1):
                month = str(month)
                if len(month) == 1:
                    month = "0" + month
                result.append(str(year)+month+day)
        else:
            for month in range (1, 13):
                month = str(month)
                if len(month) == 1:
                    month = "0" + month
                result.append(str(year)+month+day)
    return result
                    
                                
    
#def xml_to_dict(elem)
# Parse XML string
#讀取xml檔案
tree = ET.parse("data.xml")
root = tree.getroot()
# Convert XML to dictionary
#將xml轉換為字典
data_dict = xml_to_dict(root)

#print_dict(data_dict)
fields = ["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
wb = Workbook()
#建立excel檔案
sheet = wb.active
#讓excel啟動，建立第一個工作表格
sheet.title = "fields"
fillsheet(sheet, fields, 1)
#執行函式，注意參數要放對
startYear, startMonth = int(data_dict["startYear"]), int(data_dict["startMonth"])
endYear, endMonth = int(data_dict["endYear"]), int(data_dict["endMonth"])
#上面兩行為讀取字典裡的內容，讀取時順便變成正整數
yearList = returnStrDayList(startYear, startMonth, endYear, endMonth)
#執行函式
#print(yearList)
row = 2
for YearMonth in yearList:
    rq = requests.get(data_dict["url"], params={
        "response":"json",
        "date": YearMonth, 
        "stockNo": data_dict["stockNo"]})
    jsonData = rq.json()
    dailyPriceList = jsonData.get("data", [])
    for dailyPrice in dailyPriceList:
        fillsheet(sheet, dailyPrice,row)
        row +=1
    time.sleep(3)
name= data_dict["excelName"]
wb.save(name+".xlsx")
#存擋