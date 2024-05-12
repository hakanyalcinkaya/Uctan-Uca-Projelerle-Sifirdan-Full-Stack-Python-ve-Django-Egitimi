# Python: Set ile Calismak

## Icerik
- [Tuple ile Calismak](001-tuple-ile-calismak.py)

# Tuple - Cheat Sheet

Bu cheat sheet, Python'da tuple'larla çalışırken yaygın kullanılan metotların özetini verir.

- **count()**
  - Tuple içinde belirli bir elemanın kaç kez olduğunu gösterir.
  - Örnek:
    ```python
    tup1e = (1, 2, 3) 
    tup1e.count(3) 
    # 1
    ```

- **index()**
  - Tuple içinde belirli bir elemanın ilk bulunduğu indeksi döndürür.
  - Örnek:
    ```python
    tup1e = (1, 2, 3, 4, 3) 
    tup1e.index(3) 
    # 2
    ```

- **len()**
  - Tuple'ın eleman sayısını verir. 
  - Örnek:
    ```python
    tup1e = (1, 2, 3, 4, 3) 
    len(tup1e) 
    # 5
    ```

## BONUS 
  - tuple() fonksiyonu, bir liste veya başka bir iterable'ı tuple'a dönüştürür.
  - Örnek:
    ```python
    numbers = [1, 2, 3]
    tuple(numbers)
    # (1, 2, 3)
    tuple("burak") 
    # ("b", "u", "r", "a", "k")
    ```

  - Tuple, üç farklı şekilde oluşturulabilir.
  - Örnekler:
    ```python
    tup1 = (1, 2, 3)  # Normal tuple oluşturma.
    tup2 = 1, 2, 3  # Parantez olmadan da tuple oluşturulabilir.
    tup3 = ()  # Boş bir tuple oluşturur.
    ``` 
