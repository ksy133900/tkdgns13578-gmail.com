### 1. 모든 테이블의 이름을 출력하세요.
```sql
.tables
```

### 2. 모든 테이블의 데이터를 확인해보세요.
| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.

```sql
.schema 테이블명
```


### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.
```sql
SELECT * from albums ORDER by title DESC limit 5;
```

```sql
AlbumId  Title                         ArtistId
-------  ----------------------------  --------
208      [1997] Black Light Syndrome   136
240      Zooropa                       150
267      Worlds                        202
334      Weill: The Seven Deadly Sins  264
8        Warner 25 Anos                6
```

### 4. 고객(customers) 테이블의 행 개수를 출력하세요.

| 단, 컬럼명을 `고객 수`로 출력하세요.

```sql
select count(*) as '고객 수' from customers
```

```sql
고객 수
----
59
```

### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.

```sql
select FirstName, LastName from customers where Country = 'USA';
```

```sql
이름        성
--------  ----------
Frank     Harris
Jack      Smith
Michelle  Brooks
Tim       Goyer
Dan       Miller
Kathy     Chase
Heather   Leacock
John      Gordon
Frank     Ralston
Victor    Stevens
Richard   Cunningham
Patrick   Gray
Julia     Barnett
```

### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.

| 단, 컬렴명을 `송장수`로 출력하세요.

```sql
select count(*) as '송장 수' from invoices where BillingPostalCode is notnull;
```

```sql
송장 수
----
384
```

### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.

| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.

```sql
select count(*) as '송장 수' from invoices where BillingPostalCode isnull order by InvoiceDate desc limit 5;
```

```sql
InvoiceId  CustomerId  InvoiceDate          BillingAddress                            BillingCity  BillingState  BillingCountry  BillingPostalCode  Total
---------  ----------  -------------------  ----------------------------------------  -----------  ------------  --------------  -----------------  -----
410        35          2013-12-09 00:00:00  Rua dos Campeoes Europeus de Viena, 4350  Porto                      Portugal   
                        8.91
401        46          2013-11-04 00:00:00  3 Chatham Street                          Dublin       Dublin        Ireland    
                        3.96
378        46          2013-08-02 00:00:00  3 Chatham Street                          Dublin       Dublin        Ireland    
                        1.98
355        35          2013-04-10 00:00:00  Rua dos Campeoes Europeus de Viena, 4350  Porto                      Portugal   
                        13.86
344        35          2013-02-28 00:00:00  Rua dos Campeoes Europeus de Viena, 4350  Porto                      Portugal   
                        1.98
```

```
너무 길어서 잘리네요;
```





### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.

| `strftime`를 검색해서 활용해보세요.

```sql
SELECT count(*) from invoices where InvoiceDate LIKE '2013%';
```

```sql
select count(*) from invoices where strftime('%Y', InvoiceDate) = '2013';
```

```sql
count(*)
--------
80
```

### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.

```sql
select CustomerId as "고객id" , FirstName as "이름", LastName as "성"
from customers
where FirstName like 'L%'
ORDER by "고객id" ;
```

```sql
고객id  이름        성
----  --------  ---------
1     Luis      Goncalves
2     Leonie    Kohler
45    Ladislav  Kovacs
47    Lucas     Mancini
57    Luis      Rojas
```

### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.

| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.

```sql
SELECT count(*) as "고객 수" , Country as '나라'
from customers group by country ORDER by "고객 수" DESC limit 5;
```

```sql
고객 수  나라
----  --------------
13    USA
8     Canada
5     France
5     Brazil
4     Germany
```

### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

```sql
SELECT ArtistId , Count(*) as "앨범 수" FROM albums
GROUP by artistID
having count(*) = (select max(mycount)
    from (select ArtistId, count(*) as mycount
              from albums
                GROUP by ArtistId) as result);
```

```sql
ArtistId  앨범 수
--------  ----
90        21
```

### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요

| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.

```sql 
```

### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.

```sql 
select count(*) as "고객 수" , Country , state from customers
where state NOTNULL GROUP by Country , State
ORDER by "고객 수" DESC , Country desc limit 5;
```

```sql
고객 수  Country  State
----  -------  -----
3     USA      CA
3     Brazil   SP
2     Canada   ON
1     USA      WI
1     USA      WA
```

### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.

| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 

```sql 
select 
    CustomerId,
    CASE
        WHEN "FAX" isnull then "X"
        else "O"
        End As "FAX 유/무"
from customers
ORDER by CustomerId limit 5;

```

```sql
CustomerId  FAX 유/무
----------  -------
1           O
2           X
3           X
4           X
5           O
```

### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.

| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.

```sql 
SELECT
    LastName,
    FirstName,
    cast(strftime('%Y','now') as int) - cast(strftime('%Y',BirthDate) AS int) + 1 AS '나이'
from employees
ORDER by EmployeeId ;
```

```sql
LastName  FirstName  나이
--------  ---------  --
Adams     Andrew     61
Edwards   Nancy      65
Peacock   Jane       50
Park      Margaret   76
Johnson   Steve      58
Mitchell  Michael    50
King      Robert     53
Callahan  Laura      55
```

### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.

| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.

```sql 
SELECT Name from artists 
where ArtistId = ( 
    SELECT 
        ArtistId 
    from ( 
        SELECT 
            ArtistId,
            count(*) AS "앨범 수"
        from albums
        GROUP by ArtistId
        order by "앨범 수" DESC
        limit 1
    )
);
```

```sql
Name
-----------
Iron Maiden
```

### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.

| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.

```sql 
select Name
from genres
where GenreId = (
    SELECT GenreId
    from (
        SELECT
            GenreId,
            count(*) AS "개수"
        from tracks
        GROUP by GenreId
        order by "개수"
        LIMIT 1
    )
);
```

```sql
Name
-----
Opera
```



### 자유롭게 문제를 만들어 보시고, 디스코드 채널에 공유해보세요!
