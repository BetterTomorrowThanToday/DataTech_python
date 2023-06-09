import pandas as pd

# 출력 옵션 설정
pd.set_option("display.max_rows", None)  # 모든 행 표시
pd.set_option("display.max_columns", None)  # 모든 열 표시

subway_usage_query = """
INSERT into subway_usage(id, off_board, on_board, precipitation_id, subway_station_id)
VALUES (%s, %s, %s, %s, %s)
"""
