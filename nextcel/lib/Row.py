from typing import Any

class Row(list):
    def __init__(self, data: list, column: list = []) -> None:
        super().__init__(data)
        self.column = column

    def replace_all(self, target, value) -> None:
        """
        일치하는 값을 찾아 모두 치환합니다.

        예시
        --
        ```py
        # a를 b로 모두 바꿈
        row.replace_all("a", "b")

        >>> ["a", "a", 1, "a"]
        >>> ["b", "b", 1, "b"]
        """
        for i, v in enumerate(self):
            if v == target:
                self[i] = value
    
    def get(self, name) -> Any:
        """
        항목 이름으로 데이터 값에 접근합니다.

        예시
        --
        ```py
        row.get("기온(°C)")
        """
        return self[self.column.index(name)]
    