from pandas import DataFrame

from nextcel.lib.ExcelData import ExcelData

def convert(data: DataFrame) -> ExcelData:
    """
        pandas의 DataFrame을 nextcel로 조작 가능하도록 하는
        새 인스턴스를 반환합니다.
    """
    return ExcelData(data)