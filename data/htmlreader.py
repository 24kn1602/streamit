import pandas as pd

# 텍스트 파일에서 HTML 데이터 읽기
with open('data/table_data2.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# HTML 내용을 데이터프레임으로 변환
dfs = pd.read_html(html_content)

# 여러 개의 표가 있을 수 있으므로 첫 번째 표를 선택
df = dfs[0]

# 데이터프레임 출력
print(df)

df.to_csv('record.csv', index=True)