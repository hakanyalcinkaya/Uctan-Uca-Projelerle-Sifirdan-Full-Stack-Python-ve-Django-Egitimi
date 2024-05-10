# Python: Set ile Calismak

## Icerik
- [Set ile Calismak](001-set-ile-calismak.py)

- [Listeyi Sirali Getirmek](002-listeyi-sirali-getirmek.py)


# Set - Cheat Sheet

Bu cheat sheet, Python'da set'lerle çalışırken yaygın kullanılan metotların özetini verir. Yukarıdaki metotlar, kümelerle ilgili temel işlemleri kapsar.
 

- **add()**
  - Kümeye yeni tek-bir- eleman ekler.
  - Örnek:
    ```python
    s = {1, 2, 3}
    s.add(4) 
    # {1, 2, 3, 4}
    ```

- **clear()**
  - Kümeyi temizler, tüm elemanları siler.
  - Örnek:
    ```python
    s = {1, 2, 3}
    s.clear()  
    # Boş bir set
    ```
    
- **difference()**
  - Bir kümede olup diğerinde olmayan elemanları getirir.
  - Kısayol gösterimi: `-` (eksi işareti).
  - Örnek:
    ```python
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    diff = s1.difference(s2)  
    # {1, 2}
    ```

- **symmetric_difference()**
  - İki kümede ortak olmayan elemanları gösterir.
  - Kısayol gösterimi: `^` (şapka işareti).
  - Örnek:
    ```python
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    sym_diff = s1.symmetric_difference(s2)  
    # {1, 4}
    ```

- **intersection()**
  - İki kümede de ortak olan elemanları getirir.
  - Kısayol gösterimi: `&` (ve işareti).
  - Örnek:
    ```python
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    common = s1.intersection(s2)  
    # {3}
    ```

- **union()**
  - İki kümedeki tüm unique elemanları getirir.
  - Kısayol gösterimi: `|` (pipe işareti).
  - Örnek:
    ```python
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    combined = s1.union(s2)  
    # {1, 2, 3, 4, 5}
    ```
    
    ![set-diagram](000-Assets/015-Python---set-ile-Calismak/set_diagram.png) 

- **discard()**
  - Belirtilen elemanı kümeden çıkarır. Eğer eleman kümede yoksa hata vermez.
  - Örnek:
    ```python
    s = {1, 2, 3}
    s.discard(2)  # {1, 3}
    ```

- **remove()**
  - `discard()` ile benzer şekilde çalışır, ancak belirtilen eleman kümede yoksa hata verir.
  - Örnek:
    ```python
    s = {1, 2, 3}
    s.remove(2)  # {1, 3}
    # s.remove(5)  # Hata: KeyError
    ```

- **pop()**
  - Argümansız çalışır. Kümeden rastgele bir eleman çıkartır. Küme boşsa hata verir.
  - Örnek:
    ```python
    s = {1, 2, 3}
    s.pop()  
    # {3}
    ```

- **update()**
  - Mevcut kümeye eleman ekler.
  - Örnek:
    ```python
    s = {1, 2, 3}
    s.update({3, 4, 5})  
    # {1, 2, 3, 4, 5}
    ```

