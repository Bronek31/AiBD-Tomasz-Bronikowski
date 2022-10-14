# Ćwiczenie 3  Łączenie z bazą danych i instrukcja select

Celem ćwiczenia jest połączenie się z bazą danych przy użyciu bibliotek pythona i wykonanie zapytań select na przykładowej bazie danych. 

## Łączenie z bazą danych przy pomocy skryptu Python

Istnieje wiele bibliotek do obsługi połączeń Pythona z bazami danych. Na tych zajęciach będziemy korzystać z biblioteki sqlAlchemy oraz psycopg2. 

### instalacja niezbędnych pakietów
```

pip install sqlalchemy psycopg2 pandas

```

### Łączenie się za pomocą sqlAlchemy
```python

from sqlalchemy import create_engine

db_string = "postgres://postgres:admin@localhost:5432/test"

db = create_engine(db_string)

connection_sqlalchemy = db.connect()

```

Gdzie *db_string* formatowany jest w następujący sposób:

nazwa_silnika://użytkownik:hasło@adres_serwera:port/nazwa_bazy

Zapytanie do bazy danych wraz z przeglądnięciem wyników można wykonać używając skryptu:
```python

result_set = db.execute("SELECT * FROM city")  
for r in result_set:  
    print(r)

```
Fragment wyniku:
```

(1, 'A Corua (La Corua)', 87, datetime.datetime(2006, 2, 15, 9, 45, 25))
(2, 'Abha', 82, datetime.datetime(2006, 2, 15, 9, 45, 25))
(3, 'Abu Dhabi', 101, datetime.datetime(2006, 2, 15, 9, 45, 25))
...

```
Stosując tą metodę wynik zapytania do zmiennej *result_set* jest zwracany jako obiekt typu [ResultProxy](https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.ResultProxy).
### Łączenie się za pomocą psycopg2 i pandas
```python
import psycopg2 as pg
import pandas as pd

connection = pg.connect(host='localhost', port=5432, dbname='test', user='postgres', password='admin')
```

Wykonanie zapytania:
```python
df = pd.read_sql('select * from city',con=connection)
print(df)
```

Rezultat:

|     	| city_id 	|               city 	| country_id 	|         last_update 	|
|----:	|--------:	|-------------------:	|-----------:	|--------------------:	|
|   0 	|       1 	| A Corua (La Corua) 	|         87 	| 2006-02-15 09:45:25 	|
|   1 	|       2 	|               Abha 	|         82 	| 2006-02-15 09:45:25 	|
|   2 	|       3 	|          Abu Dhabi 	|        101 	| 2006-02-15 09:45:25 	|
|   3 	|       4 	|               Acua 	|         60 	| 2006-02-15 09:45:25 	|
|   4 	|       5 	|              Adana 	|         97 	| 2006-02-15 09:45:25 	|
| ... 	|     ... 	|                ... 	|        ... 	|                 ... 	|

W tym przypadku wyniki zapisywany jest w postaci obiektu [DataFeram](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame) z biblioteki [pandas](https://pandas.pydata.org).

Dodatkowo możliwe jest użycie pandasa i sqlAlchemy, przykład użycia tego mechanizmu znajduje się w notatniku example.

## Baza ćwiczeniowa

W części poświęconej bazom danych na zajęciach będziemy używać bazy z oficjalnego tutorialu PostgeSQL dostępnej [tutaj](https://www.postgresqltutorial.com/postgresql-sample-database/).

## Dane do połączenia do bazy zdalnej
	- host: pgsql-196447.vipserv.org
	- port: 5432
	- login: wbauer_adb
	- hasło: adb2020
	- nazwa_bazy: wbauer_adb

## Polecenie SELECT

Jednym z najczęstszych zadań podczas pracy z bazami danych jest wyszukiwanie danych  za pomocą instrukcji SELECT. Instrukcja SELECT jest jedną z najbardziej złożonych instrukcji w PostgreSQL. Zawiera wiele klauzul umożliwiających utworzenie elastycznych zapytań.

Instrukcja SELECT zawiera następujące klauzule:

- DISTINCT - wypisz .
- ORDER BY - sortuj po wybranej kolumnie.
- WHERE.- filtrowanie według wartości logicznych
- LIMIT lub FETCH -wybieranie podzbiór wierszy z tabeli wynikowej
- GROUP BY - grupowanie wiersze według zadanej kolumny
- HAVING - filtrowanie ze zbioru .
- Łączenie z innymi tabelami za pomocą złączeń: INNER JOIN, LEFT JOIN, FULL OUTER JOIN, CROSS JOIN.

### Podstawowa składnia SELECT

```sql
SELECT
   column_1,
   column_2,
   ...
FROM
   table_name;
```

#### Przykład użycia

Wypisanie wybranych kolumny z zadanej tabeli:

```sql
SELECT
   first_name,
   last_name,
   email
FROM
   customer;
```

Wypisanie wszystkich kolumny z zadanej tabeli:

```sql
SELECT
   *
FROM
   customer;
```

### Klauzula ORDER BY

Klauzula ORDER BY pozwala sortować wiersze zwrócone z instrukcji SELECT w kolejność rosnąca lub malejąca na podstawie określonych kryteriów i kolumny.

#### Składnia ogólna:

```sql
SELECT
   column_1,
   column_2
FROM
   tbl_name
ORDER BY
   column_1 ASC,
   column_2 DESC;
```

W przypadku podania więcej niż jednej kolumny w klauzuli ORDER BY zbiór zostanie posortowany względem kolejnych kolumny. Znacznik ASC  odpowiada za sortowanie rosnące i jest domyślną wartością. DESC sortuje zbiór malejąco.

### Klauzula DISTINCT

Klauzula DISTINCT jest używana w instrukcji SELECT do usuwania zduplikowanych wierszy z wyniku zapytania. Klauzula DISTINCT zachowuje jeden wiersz dla każdej grupy duplikatów. Klauzula DISTINCT może być używane dla jednej lub więcej kolumn tabeli.

#### Składnia ogólna:

```sql
SELECT
 DISTINCT column_1
FROM
 table_name;
```

#### Przykłady użycia:

Dla więcej niż jednej kolumny:

```sql
SELECT
 DISTINCT column_1,
 column_2
FROM
 tbl_name;
```

Dla dokładnie jednej kolumny i pokazanie pozostałych:

```sql
SELECT
 DISTINCT ON
 (column_1) column_1_alias,
 column_2
FROM
 tbl_name
```

### Klauzula WHERE

Klauzula WHERE pojawia się zaraz po klauzuli FROM w instrukcji SELECT. Klauzula WHERE jest znacznikiem wykorzystania warunków filtrowania wierszy zwróconych z instrukcji SELECT.

Warunek musi mieć wartość prawda, fałsz lub nieznany. Może to być wyrażenie boolowskie lub kombinacja wyrażeń boolowskich przy użyciu operatorów AND i OR.

Zapytanie zwraca wiersze spełniające warunek w klauzuli WHERE. Innymi słowy, tylko wiersze, które powodują spełnienie warunku, zostaną uwzględnione w zestawie wyników.

Oprócz instrukcji SELECT można użyć klauzuli WHERE w instrukcji UPDATE i DELETE, aby określić wiersze do aktualizacji lub usunięcia.

#### Składnia ogólna:

```sql
SELECT select_list
FROM table_name
WHERE condition;
```

|Operator|Opis|
|-|-|
|=|Równy|
|>|większy niż|
|<|mniejszy niż|
|>=| większy bądź równy|
|<=| mniejszy bądź równy|
|<> lub !=| różny|
|AND| operator AND|
|OR|operator OR|

### Klauzula OFFSET

LIMIT jest opcjonalną klauzulą instrukcji SELECT, która pomija n pierwszych wierszy.
####  Składnia ogólna:

```sql
SELECT
   *
FROM
   table
OFFSET n;
```

### Klauzula LIMIT

LIMIT jest opcjonalną klauzulą instrukcji SELECT, która zwraca n pierwszych wierszy z zapytania.

####  Składnia ogólna:

```sql
SELECT
   *
FROM
   table_name
LIMIT n;
```

Jeśli chcemy pominąć liczbę wierszy przed zwróceniem n wierszy, użyj klauzuli OFFSET umieszczonej po klauzuli LIMIT jak w następującej instrukcji:

```sql
SELECT
   *
FROM
   table
LIMIT n OFFSET m;
```

### Klauzula FETCH 

Klauzula FETCH umożliwia pobrania części wierszy zwróconych przez zapytanie. 

```sql
OFFSET start { ROW | ROWS }
FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY
```

#### Przykłady użycia:

```sql
SELECT
    film_id,
    title
FROM
    film
ORDER BY
    title 
FETCH FIRST ROW ONLY;


SELECT
    film_id,
    title
FROM
    film
ORDER BY
    title 
FETCH FIRST 5 ROW ONLY;
```

### Klauzula IN

Umożliwia sprawdzenie czy dana kolumna zawiera wartość ze zbioru: value IN (value1,value2,...), lub w wersji przeciwnej czy nie należy do zbioru: value NOT IN (value1,value2,...),

#### Przykłady użycia:

```sql
SELECT
 customer_id,
   rental_id,
   return_date
FROM
   rental
WHERE
   customer_id IN (1, 2)
ORDER BY
   return_date DESC;
```

### Klauzula BETWEEN

Sprawdza czy wartość znajduje się w zadanym przedziale: value BETWEEN low AND high; lub przeciwnie value NOT BETWEEN low AND high

#### Przykłady użycia:

```sql
SELECT
   customer_id,
   payment_id,
   amount
FROM
   payment
WHERE
   amount BETWEEN 8
AND 9;
```

## Ćwiczenie:
Wykonaj zapytania za pomocą skryptów pythona:

1. Ile kategorii filmów mamy w wypożyczalni?
2. Wyświetl listę kategorii w kolejności alfabetycznej.
3. Znajdź najstarszy i najmłodszy film do wypożyczenia.
4. Ile wypożyczeń odbyło się między 2005-07-01 a 2005-08-01?
5. Ile wypożyczeń odbyło się między 2010-01-01 a 2011-02-01?
6. Znajdź największą płatność wypożyczenia.
7. Znajdź wszystkich klientów z Polski, Nigerii lub Bangladeszu.
8. Gdzie mieszkają członkowie personelu?
9. Ilu pracowników mieszka w Argentynie lub Hiszpanii?
10. Jakie kategorie filmów zostały wypożyczone przez klientów?
11. Znajdź wszystkie kategorie filmów wypożyczonych w Ameryce.
12. Znajdź wszystkie tytuły filmów, w których grał: Olympia Pfeiffer lub Julia Zellweger lub Ellen Presley
