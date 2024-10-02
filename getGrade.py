import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


def getGrade(url, username, password):
    # 使用 HTTP Basic Authentication 登入並發送請求
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # 檢查狀態碼來判斷是否登入成功
    if response.status_code != 200:
        print(f"登入失敗，狀態碼：{response.status_code}")
        return

    print("登入成功！")
    soup = BeautifulSoup(response.text, 'html.parser')
    table_body = soup.find('table', class_='table-striped').find('tbody')
    # print(table_body)
    # 確認 table 是否存在
    if table_body:
        rows = table_body.find_all('tr')  # 找到所有的表格列 (tr)

        # 解析每個 row，略過第一個表頭列
        result = []
        for row in rows:  # 跳過表頭列
            columns = row.find_all('td')  # 找到該列中的所有欄位 (td)
            if len(columns) >= 6:  # 確保至少有 6 個欄位（對應 3, 4, 5, 6）
                # 取得第 3, 4, 5, 6 個欄位中的 <a> 文字
                sid = columns[2].find('a').get_text(strip=True)  # 第 3 欄 SID
                pid = columns[3].find('a').get_text(strip=True)  # 第 4 欄 PID
                lang = columns[4].find('a').get_text(strip=True)  # 第 5 欄 Lang
                
                # 第 6 欄 Result，需要進一步取得 <span> 中的文字
                result_text = columns[5].find('a').find('span').get_text(strip=True)

                # 以字典形式儲存每列的資料
                result.append({
                    'sid': sid,
                    'pid': pid,
                    'lang': lang,
                    'result': result_text
                })
        return result
    else:
        print("找不到目標 table。")
