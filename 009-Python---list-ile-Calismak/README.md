# Python: list ile Calismak

## Icerik
- [list Nedir ve Nasil Tanimlanir](001-list-Nedir-ve-Nasil-Tanimlanir.py)
- [list Icine Oge Eklemek, Cikartmak ve Erismek](002-list-Icine-Oge-Eklemek-Cikartmak-Erismek.py)
- [list-leri Kopyalamak, Birlestirmek ve IcIce Listelerle Calismak](003-list-leri-Kopyalamak-Birlestirmek-ve-IcIce-Liste-Tanimlamak.py)
- [Bilinmesi Gereken list Metodlari](004-Bilinmesi-Gereken-list-Metodlari.py)


# List - Cheat Sheet

Bu cheat sheet, Python'da list'lerle çalışırken yaygın kullanılan metotların özetini verir.

- **append()**
  - Listenin sonuna yeni tek-bir- eleman ekler.
  - Örnek:
    ```python
    numbers = [1, 2, 3]

    numbers.append(4) 
    # numbers = [1, 2, 3, 4]
    ```

- **insert()**
  - Listenin belirtilen indeksine tek-bir- eleman ekler. İlk argüman eklenmesi istenen değer, virgülden sonraki ise indeks bilgisidir.
  - Örnek:
    ```python
    numbers = [1, 2, 3]

    numbers.insert(99, 2) 
    # numbers = [1, 2, 99, 3]
    ```

- **remove()**
  - Belirtilen değere sahip ilk elemanı siler.
  - Örnek:
    ```python
    numbers = [1, 2, 3, 2]

    numbers.remove(2) 
    # numbers = [1, 3, 2]
    ```

- **pop()**
  - Indekse göre silme işlemi yapar. Belirtilen indeksteki elemanı siler ve döndürür. Indeks belirtilmemişse listenin en son elemanını siler. Bu değer tutulmak istenirse bir değişkene atanabilir.
  - Örnek:
    ```python
    numbers = [1, 2, 3, 2]

    popped_item = numbers.pop() 
    # popped_item = 2
    # numbers = [1, 2, 3]
    # numbers.pop(0) --> 1
    ```

- **clear()**
  - Listenin tüm elemanlarını siler.
  - Örnek:
    ```python
    numbers = [1, 2, 3, 2]

    numbers.clear() 
    # []
    ```

- **count()**
  - Belirtilen elemanın, liste içinde kaç kez geçtiğini sayar ve bu sayıyı döndürür.
  - Örnek:
    ```python
    numbers = [1, 2, 3, 2, 4, 2]

    numbers.count(2) 
    # 3
    ```

- **index()**
  - Belirtilen değere sahip ilk elemanın indeks bilgisini verir.
  - Örnek:
    ```python
    numbers = [1, 2, 3, 2, 4, 2]

    numbers.index(2) 
    # 1
    ```

- **reverse()**
  - Listenin elemanlarını tersten yazarak değiştirir.
  - Örnek:
    ```python
    numbers = [1, 2, 3, 2, 4, 2]

    numbers.reverse() 
    # numbers = [2, 4, 2, 3, 2, 1]
    ```

- **sort()**
  - Bir listeyi sıralar. Varsayılan olarak, sayılar küçükten büyüğe ve metinler alfabetik olarak sıralanır. Reverse parametresi True olarak ayarlanırsa, sıralama tersine çevrilir.
  - Örnek:
    ```python
    numbers = [3, 1, 4, 2]

    numbers.sort()  
    # numbers = [1, 2, 3, 4]

    numbers = [3, 1, 4, 2]
    
    numbers.sort(reverse=True)  
    # numbers = [4, 3, 2, 1]

    fruits = ['banana', 'apple', 'cherry']

    fruits.sort()  
    # fruits = ['apple', 'banana', 'cherry']
    ```

- **extend()**
  - Bir listenin sonuna, başka bir iterable'ın (liste-tuple-string vb.) tüm elemanlarını ekler. Bu işlem, listenin orijinal halini değiştirir.
  - Örnek:
    ```python
    numbers = [1, 2, 3]

    numbers.extend([4, 5, 6])  
    # numbers = [1, 2, 3, 4, 5, 6]
    
    numbers.extend("word")
    # numbers = [1, 2, 3, 4, 5, 6, "w", "o", "r", "d"]
    ```