# ExcelData


## ExcelData.pandas

### 설명

pandas 라이브러리의 기능을 사용할 때 접근할 속성입니다.


## ExcelData.get_row()

### 설명
데이터의 n번째 줄을 불러옵니다. (인덱스로 취급)

### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")

row_0 = data.get_row(0)

print(row_0)
```

### 출력
```
[108, '서울', Timestamp('2022-08-15 01:00:00'), 27.4, 'null', 'null', 'null', 2.1, 'null', 180, 'null', 84, 'null', 30.6, 24.4, 994.6, 'null', 1004.2, 'null', 'null', 9.0, 'null', 9.0, 'null', 'null', 10, 10, 'null', 5, 2000, 'null', 'null', 26.2, 'null', 28.1, 27.9, 27.4, 27.3]
```

## ExcelData.names

### 설명

데이터의 항목 이름(column)들

### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")

print(data.names)
```
### 출력

```
['지점', '지점명', '일시', '기온(°C)', '기온 QC플래그', '강수량(mm)', '강수량 QC플래그', '풍속(m/s)', '풍속 QC플래그', '풍향(16방위)', '풍향 QC플래그', '습도(%)', '습도 QC플래그', '증기압(hPa)', '이슬점온도(°C)', '현지기압(hPa)', '현지
기압 QC플래그', '해면기압(hPa)', '해면기압 QC플래그', '일조(hr)', '일조 QC플래그', '일사(MJ/m2)', '일사 QC플래그', '적설(cm)', '3시간신적설(cm)', '전운량(10분위)', '중하층운량(10분위)', '운형(운형약어)', '최저운고(100m )', '시정(10m)', 
'지면상태(지면상태코드)', '현상번호(국내식)', '지면온도(°C)', '지면온도 QC플래그', '5cm 지중온도(°C)', '10cm 지중온도(°C)', '20cm 지중온도(°C)', '30cm 지중온도(°C)']
```

## ExcelData.find_by_value()

### 설명

데이터들 중 특정 항목의 값이 원하는 값과 일치하는 것들만 모아서 가져옵니다.

### 예시

```py
import nextcel

data = nextcel.load_excel("data.xlsx")
found = data.find_by_value(name="해면기압(hPa)", value=999)

print(found)
```

### 출력
```
[[108, '서울', Timestamp('2022-08-15 14:00:00'), 29.5, 'null', 'null', 'null', 6.3, 'null', 180, 'null', 77, 'null', 31.7, 25.0, 989.5, 'null', 999.0, 'null', 0.0, 'null', 0.93, 'null', 'null', 'null', 10, 9, 'ScAs', 7, 2000, 'null', 'null', 29.3, 'null', 28.7, 28.1, 27.0, 26.9]]
```

## ExcelData.filter()

### 설명

데이터들 중 특정 조건을 만족하는 항목들만 모아서 가져옵니다.

### 예시

```py
import nextcel

data = nextcel.load_excel("data.xlsx")

filtered = data.filter(lambda row: row.get("습도(%)") > 90)

print(filtered)
```

### 출력
```
[[108, '서울', Timestamp('2022-08-15 19:00:00'), 27.9, 'null', 0.7, 'null', 6.2, 'null', 230, 'null', 91, 'null', 34.0, 26.2, 988.0, 'null', 997.5, 'null', 0.0, 'null', 0.03, 'null', 'null', 'null', 10, 9, 'StNs', 4, 1034, 'null', 1.0, 
26.7, 'null', 28.3, 28.0, 27.2, 27.1], [108, '서울', Timestamp('2022-08-15 20:00:00'), 27.7, 'null', 0.0, 'null', 6.1, 'null', 230, 'null', 91, 'null', 33.6, 26.0, 988.8, 'null', 998.3, 'null', 0.0, 'null', 0.0, 'null', 'null', 'null', 
10, 9, 'ScAs', 6, 1878, 'null', 1.0, 26.6, 'null', 28.1, 27.8, 27.2, 27.1], [108, '서울', Timestamp('2022-08-15 23:00:00'), 27.3, 'null', 0.2, 'null', 2.8, 'null', 250, 'null', 91, 'null', 32.8, 25.6, 989.6, 'null', 999.2, 'null', 'null', 9.0, 'null', 9.0, 'null', 'null', 10, 9, 'ScAs', 6, 877, 'null', 1901.0, 26.4, 'null', 27.7, 27.5, 27.0, 27.1]]
```

## ExcelData.sort_by_value()

### 설명

데이터들을 특정 항목을 기준으로 정렬합니다.

### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")

data.sort_by_value("기온(°C)")

print(data)
```

### 출력

```
                                  <기온(°C)>
23  108  서울 2022-08-16 00:00:00    26.6     null     0.0      null      3.1     null       270  ...           7     1612         null     1901.0      25.8        null         27.6           27.4          27.0          27.1
22  108  서울 2022-08-15 23:00:00    27.3     null     0.2      null      2.8     null       250  ...           6      877         null     1901.0      26.4        null         27.7           27.5          27.0          27.1
4   108  서울 2022-08-15 05:00:00    27.3     null    null      null      3.9     null       200  ...           6     2000         null       null      25.6        null         27.6           27.5          27.1          27.2
3   108  서울 2022-08-15 04:00:00    27.3     null    null      null      5.0     null       200  ...           6     2000         null       null      25.7        null         27.8           27.6          27.2          27.2
0   108  서울 2022-08-15 01:00:00    27.4     null    null      null      2.1     null       180  ...           5     2000         null       null      26.2        null         28.1           27.9          27.4          27.3
1   108  서울 2022-08-15 02:00:00    27.4     null    null      null      4.0     null       200  ...           5     2000         null       null      25.9        null         28.0           27.8          27.3          27.3
2   108  서울 2022-08-15 03:00:00    27.4     null    null      null      3.5     null       200  ...           6     2000         null       null      25.8        null         27.9           27.7          27.2          27.2
5   108  서울 2022-08-15 06:00:00    27.5     null    null      null      5.4     null       200  ...           6     2000         null       null      25.6        null         27.6           27.4          27.0          27.1
6   108  서울 2022-08-15 07:00:00    27.6     null    null      null      5.6     null       200  ...           6     2000         null       null      26.1        null         27.5           27.3          26.9          27.1
7   108  서울 2022-08-15 08:00:00    27.7     null    null      null      5.1     null       200  ...           6     2000         null       null      26.3        null         27.5           27.3          26.9          27.1
21  108  서울 2022-08-15 22:00:00    27.7     null     0.0      null      3.2     null       230  ...           6     1914         null        1.0      26.4        null         27.8           27.6          27.1          27.1
20  108  서울 2022-08-15 21:00:00    27.7     null    null       9.0      5.2     null       230  ...           7     2000         null       null      26.4        null         27.9           27.7          27.1          27.1
19  108  서울 2022-08-15 20:00:00    27.7     null     0.0      null      6.1     null       230  ...           6     1878         null        1.0      26.6        null         28.1           27.8          27.2          27.1
(이후 생략..)
```

## ExcelData.replace_value()

### 설명

데이터의 특정 값을 모두 치환합니다.

### 예시
```py
import nextcel

data = nextcel.load_excel("data.xlsx")

data.replace_value(nextcel.null, -100)

print(data)
```

### 출력
```
0   108  서울 2022-08-15 01:00:00    27.4      -100   -100.0     -100.0      2.1      -100       180  ...            5     2000          -100     -100.0      26.2        -100          28.1           27.9           27.4           27.3   
1   108  서울 2022-08-15 02:00:00    27.4      -100   -100.0     -100.0      4.0      -100       200  ...            5     2000          -100     -100.0      25.9        -100          28.0           27.8           27.3           27.3   
2   108  서울 2022-08-15 03:00:00    27.4      -100   -100.0     -100.0      3.5      -100       200  ...            6     2000          -100     -100.0      25.8        -100          27.9           27.7           27.2           27.2   
3   108  서울 2022-08-15 04:00:00    27.3      -100   -100.0     -100.0      5.0      -100       200  ...            6     2000          -100     -100.0      25.7        -100          27.8           27.6           27.2           27.2   
4   108  서울 2022-08-15 05:00:00    27.3      -100   -100.0     -100.0      3.9      -100       200  ...            6     2000          -100     -100.0      25.6        -100          27.6           27.5           27.1           27.2   
5   108  서울 2022-08-15 06:00:00    27.5      -100   -100.0     -100.0      5.4      -100       200  ...            6     2000          -100     -100.0      25.6        -100          27.6           27.4           27.0           27.1   
6   108  서울 2022-08-15 07:00:00    27.6      -100   -100.0     -100.0      5.6      -100       200  ...            6     2000          -100     -100.0      26.1        -100          27.5           27.3           26.9           27.1   
7   108  서울 2022-08-15 08:00:00    27.7      -100   -100.0     -100.0      5.1      -100       200  ...            6     2000          -100     -100.0      26.3        -100          27.5           27.3           26.9           27.1   
8   108  서울 2022-08-15 09:00:00    28.1      -100   -100.0     -100.0      4.6      -100       200  ...            6     2000          -100     -100.0      27.4        -100          27.5           27.2           26.8           27.0   
9   108  서울 2022-08-15 10:00:00    28.6      -100   -100.0     -100.0      6.3      -100       200  ...            7     2000          -100     -100.0      28.5        -100          27.7           27.3           26.8           27.0   
10  108  서울 2022-08-15 11:00:00    29.1      -100   -100.0     -100.0      6.4      -100       200  ...            7     2000          -100     -100.0      30.0        -100          27.9           27.4           26.8           27.0   
11  108  서울 2022-08-15 12:00:00    29.5      -100   -100.0     -100.0      5.7      -100       200  ...            7     2000          -100     -100.0      30.6        -100          28.2           27.6           26.8           26.9   
12  108  서울 2022-08-15 13:00:00    29.6      -100   -100.0     -100.0      6.8      -100       180  ...            7     2000          -100     -100.0      30.3        -100          28.5           27.9           26.9           27.0   
(이후 생략...)
```

## ExcelData.replace_column()

### 설명

특정 항목의 값들을 모두 치환합니다.

### 예시

```py
import nextcel

data = nextcel.load_excel("data.xlsx")

data.replace_column("기온(°C)", 0)

print(data)
```

### 출력
```
                                  <기온(°C)>
0   108  서울 2022-08-15 01:00:00     0.0     null    null      null      2.1     null       180  ...           5     2000         null       null      26.2        null         28.1           27.9          27.4          27.3
1   108  서울 2022-08-15 02:00:00     0.0     null    null      null      4.0     null       200  ...           5     2000         null       null      25.9        null         28.0           27.8          27.3          27.3
2   108  서울 2022-08-15 03:00:00     0.0     null    null      null      3.5     null       200  ...           6     2000         null       null      25.8        null         27.9           27.7          27.2          27.2
3   108  서울 2022-08-15 04:00:00     0.0     null    null      null      5.0     null       200  ...           6     2000         null       null      25.7        null         27.8           27.6          27.2          27.2
4   108  서울 2022-08-15 05:00:00     0.0     null    null      null      3.9     null       200  ...           6     2000         null       null      25.6        null         27.6           27.5          27.1          27.2
5   108  서울 2022-08-15 06:00:00     0.0     null    null      null      5.4     null       200  ...           6     2000         null       null      25.6        null         27.6           27.4          27.0          27.1
6   108  서울 2022-08-15 07:00:00     0.0     null    null      null      5.6     null       200  ...           6     2000         null       null      26.1        null         27.5           27.3          26.9          27.1
7   108  서울 2022-08-15 08:00:00     0.0     null    null      null      5.1     null       200  ...           6     2000         null       null      26.3        null         27.5           27.3          26.9          27.1
8   108  서울 2022-08-15 09:00:00     0.0     null    null      null      4.6     null       200  ...           6     2000         null       null      27.4        null         27.5           27.2          26.8          27.0
9   108  서울 2022-08-15 10:00:00     0.0     null    null      null      6.3     null       200  ...           7     2000         null       null      28.5        null         27.7           27.3          26.8          27.0
10  108  서울 2022-08-15 11:00:00     0.0     null    null      null      6.4     null       200  ...           7     2000         null       null      30.0        null         27.9           27.4          26.8          27.0
11  108  서울 2022-08-15 12:00:00     0.0     null    null      null      5.7     null       200  ...           7     2000         null       null      30.6        null         28.2           27.6          26.8          26.9
12  108  서울 2022-08-15 13:00:00     0.0     null    null      null      6.8     null       180  ...           7     2000         null       null      30.3        null         28.5           27.9          26.9          27.0
13  108  서울 2022-08-15 14:00:00     0.0     null    null      null      6.3     null       180  ...           7     2000         null       null      29.3        null         28.7           28.1          27.0          26.9
(이후 생략...)
```
## ExcelData.replace_column_cond()

### 설명

특정 항목의 데이터들 중 조건을 만족하는 값을 모두 치환합니다.

### 예시

```py
import nextcel

data = nextcel.load_excel("자료.xlsx")
data.replace_column_cond("강수량(mm)", lambda value: value == nextcel.null, 0)

print(data)
```

### 출력
```                     
                                                   <강수량(mm)>  
0   108  서울 2022-08-15 01:00:00    27.4     null       0      null      2.1     null       180  ...           5     2000         null       null      26.2        null         28.1           27.9          27.4          27.3
1   108  서울 2022-08-15 02:00:00    27.4     null       0      null      4.0     null       200  ...           5     2000         null       null      25.9        null         28.0           27.8          27.3          27.3
2   108  서울 2022-08-15 03:00:00    27.4     null       0      null      3.5     null       200  ...           6     2000         null       null      25.8        null         27.9           27.7          27.2          27.2
3   108  서울 2022-08-15 04:00:00    27.3     null       0      null      5.0     null       200  ...           6     2000         null       null      25.7        null         27.8           27.6          27.2          27.2
4   108  서울 2022-08-15 05:00:00    27.3     null       0      null      3.9     null       200  ...           6     2000         null       null      25.6        null         27.6           27.5          27.1          27.2
5   108  서울 2022-08-15 06:00:00    27.5     null       0      null      5.4     null       200  ...           6     2000         null       null      25.6        null         27.6           27.4          27.0          27.1
6   108  서울 2022-08-15 07:00:00    27.6     null       0      null      5.6     null       200  ...           6     2000         null       null      26.1        null         27.5           27.3          26.9          27.1
7   108  서울 2022-08-15 08:00:00    27.7     null       0      null      5.1     null       200  ...           6     2000         null       null      26.3        null         27.5           27.3          26.9          27.1
8   108  서울 2022-08-15 09:00:00    28.1     null       0      null      4.6     null       200  ...           6     2000         null       null      27.4        null         27.5           27.2          26.8          27.0
9   108  서울 2022-08-15 10:00:00    28.6     null       0      null      6.3     null       200  ...           7     2000         null       null      28.5        null         27.7           27.3          26.8          27.0
(이후 생략...)
```
## ExcelData.count_null()

### 설명

항목별로 빈 값(null)의 총 합을 계산합니다.

### 예시

```py
import nextcel

data = nextcel.load_excel("자료.xlsx")

print(data.count_null())
```

### 출력
```
지점   0
지점명   0
일시   0
기온(°C)   0
기온 QC플래그   24
강수량(mm)   18
강수량 QC플래그   23
풍속(m/s)   0
풍속 QC플래그   24
풍향(16방위)   0
풍향 QC플래그   24
습도(%)   0
습도 QC플래그   24
증기압(hPa)   0
(이후 생략...)
```

## ExcelData.interpolate()

### 설명
비어있는 값을 보간합니다.  
기본 보간 방식에서, **이전 값과 다음 값이 모두 비어있을 경우 보간되지 않습니다.**

### 예시

```py
import nextcel

data = nextcel.load_excel("자료.xlsx")

data.interpolate(exclude=["일시", "운형(운형약어)"]) # 값이 숫자가 아닌 것은 제외

print(data)
```

## ExcelData.interpolate_column()

### 설명

특정 항목의 비어있는 값을 보간합니다.

### 예시

```py
import nextcel
data = nextcel.load_excel("자료.xlsx")

data.interpolate_column("풍속(m/s)")
```

## ExcelData.delete_column()

### 설명

특정 항목 전체를 삭제합니다.

### 예시

```py
import nextcel
data = nextcel.load_excel("자료.xlsx")

data.delete_column("일시")

print(data)
```

### 출력
```
0   108  서울    27.4       NaN      NaN        NaN      2.1       NaN       180       NaN  ...            5     2000           NaN        NaN      26.2         NaN          28.1           27.9           27.4
1   108  서울    27.4       NaN      NaN        NaN      4.0       NaN       200       NaN  ...            5     2000           NaN        NaN      25.9         NaN          28.0           27.8           27.3
2   108  서울    27.4       NaN      NaN        NaN      3.5       NaN       200       NaN  ...            6     2000           NaN        NaN      25.8         NaN          27.9           27.7           27.2
3   108  서울    27.3       NaN      NaN        NaN      NaN       NaN       200       NaN  ...            6     2000           NaN        NaN      25.7         NaN          27.8           27.6           27.2
4   108  서울    27.3       NaN      NaN        NaN      3.9       NaN       200       NaN  ...            6     2000           NaN        NaN      25.6         NaN          27.6           27.5           27.1
5   108  서울    27.5       NaN      NaN        NaN      5.4       NaN       200       NaN  ...            6     2000           NaN        NaN      25.6         NaN          27.6           27.4           27.0
(이후 생략...)
```