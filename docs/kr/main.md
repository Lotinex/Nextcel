# nextcel

## nextcel.isnan()

### 설명
주어진 값이 nan인지 검사합니다.

### 예시
```py
import nextcel

nextcel.isnan(10) # False
```

## nextcel.load_excel()

### 설명
지정한 경로의 엑셀 파일을 불러옵니다.
        
### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")
```

## nextcel.convert()

### 설명
pandas 데이터를 nextcel에서 조작할 수 있도록 변환합니다.

### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")

data = nextcel.convert(data.pandas.fillna(0))
```
