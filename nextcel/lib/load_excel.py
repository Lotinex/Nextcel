import pandas

from nextcel.lib.ExcelData import ExcelData
def load_excel(path: str) -> ExcelData:
    """
        지정한 경로의 엑셀 파일을 불러옵니다.
        
        예시
        --
        ```py
        data = load_excel("자료.xlsx")
        ```
    """
    return ExcelData(pandas.read_excel(path))