# DomJudge Grade Helper

### 功能
幫助我們快速拿到學生成績統計。每次執行都會產生一個新的 Excel，不會複寫，方便查看紀錄。

### 使用說明
#### 套件與版本
python 3.12

套件使用 [Poetry](https://python-poetry.org/) 或是 Pip 都行
```shell
# Poetry

poetry init
poetry shell
poetry install --no-root
```

```shell
# Pip

python3.12 -m venv venv
source venv/bin/activate  #mac
pip install -r requirements.txt
```

#### 執行
```python
python calculateGrade.py  
```

接著就會在專案中看到 `files` 這個資料夾，裡面就有整理好的 Excel，檔名使用時間和 scope 命名。
