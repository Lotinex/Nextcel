# Row

## Row.get()

### 설명

항목의 이름으로 값에 접근합니다.

### 예시

```py
import nextcel

data = nextcel.load_excel("data.xlsx")

row = data.get_row(0)
date = row.get("일시")

print(date)
```

### 출력

```
2022-08-15 01:00:00
```

## Row.replace_all()

### 설명

일치하는 값을 찾아 모두 치환합니다.

### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")

row = data.get_row(0)
row.replace_all(nextcel.null, -1)

print(row_0)
```

### 출력
```
[108, '서울', Timestamp('2022-08-15 01:00:00'), 27.4, -1, -1, -1, 2.1, -1, 180, -1, 84, -1, 30.6, 24.4, 994.6, -1, 1004.2, -1, -1, 9.0, -1, 9.0, -1, -1, 10, 10, -1, 5, 2000, -1, -1, 26.2, -1, 28.1, 27.9, 27.4, 27.3]
```
