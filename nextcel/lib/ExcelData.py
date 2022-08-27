from pandas import DataFrame
from typing import Any, Callable, Iterator

from nextcel.lib.Row import Row

class ExcelData:
    def __init__(self, data: DataFrame) -> None:
        self.data = data.fillna("null")
    def get_row(self, index: int) -> Row:
        """
            데이터의 n번째 줄을 불러옵니다. (인덱스로 취급)

            예시
            --
            ```py
            import nextcel
            data = nextcel.load_excel("자료.xlsx")
            print(data.get_row(0)) #첫번째 줄

            >>> [108, '서울', Timestamp('2022-08-15 14:00:00'), 27.4 ...]
            ```
        """
        return Row(self.data.values[index], self.names)

    @property
    def names(self) -> list:
        return self.data.head(0).columns.values.tolist()

    def find_by_value(self, **args) -> list[Row]:
        """
            데이터들 중 특정 항목의 값이 원하는 값과 일치하는 것들만 모아서 가져옵니다.

            예시
            --
            ```py
            import nextcel
            data = nextcel.load_excel("자료.xlsx")

            found = data.find_by_value(name="해면기압(hPa)", value=999)
            print(a)

            >>> [[108, '서울', Timestamp('2022-08-15 14:00:00'), 29.5, 'null' ...]]
        """
        R = []
        for row in self.data.values.tolist():
            index = self.names.index(args["name"])
            if args["value"] in row and row[index] == args["value"]:
                R.append(Row(row, self.names))
        return R
    
    def sort_by_value(self, name: str) -> None:
        """
            데이터들을 특정 항목을 기준으로 정렬합니다.

            예시
            --
            ```py
            import nextcel
            data = nextcel.load_excel("자료.xlsx")

            data.sort_by_value("기온(°C)")
        """
        self.data = self.data.sort_values(by=name)

    def __iter__(self) -> Iterator[Row]:
        for row in self.data.values.tolist():
            yield Row(row, self.names)

    def filter(self, fn: Callable[[Row], bool]) -> list[Row]:
        """
            데이터들 중 특정 조건을 만족하는 항목들만 모아서 가져옵니다.

            예시
            --
            ```py
            import nextcel
            data = nextcel.load_excel("자료.xlsx")

            # 데이터들 중 기온이 27.3 초과인 것들만 가져옴
            filtered = data.filter(lambda row: row.get("기온(°C)") > 27.3) 

            >>> [[108, '서울', Timestamp('2022-08-15 04:00:00'), 27.4, 'null', ...]]

        """
        R = []
        for row in self.data.values.tolist():
            _row = Row(row, self.names)
            if fn(_row):
                R.append(_row)
        return R

    def replace_value(self, target: Any, value: Any) -> None:
        """
            특정 값을 모두 치환합니다.

            예시
            --
            ```py
            import nextcel
            data = nextcel.load_excel("자료.xlsx")

            data.replace_value(27.4, 100)
            ```
        """
        self.data = self.data.replace(target, value)

    def __repr__(self): # DataFrame으로 내보냄
        return self.data.__repr__()


    def replace_column(self, column: str, value: Any) -> None:
        """
            특정 항목의 값을 모두 치환합니다.

            예시
            --
            ```py
            import nextcel
            data = nextcel.load_excel("자료.xlsx")

            data.replace_column("기온(°C)", 100)
        """
        for i, e in enumerate(self.data[column]):
            self.data[column][i] = value


