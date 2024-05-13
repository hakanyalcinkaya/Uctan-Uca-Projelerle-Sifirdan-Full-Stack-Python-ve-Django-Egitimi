# Python: Dict ile Calismak

## Icerik
- [Dict Olusturmak ve Ogelere Erismek](001-dict-olusturmak-ve-ogelere-erismek.py)
- [Dict get() Kullanimi](002-dict-get-kullanimi.py)
- [Dict Icindeki Verilerin For Ile Kullanimi](003-dict-icindeki-verilerin-for-ile-kullanilmasi.py)
- [Dict Tanimlamanin Alternatif Yolu](004-dict-tanimlamanin-alternatif-yolu.py)

# Dict - Cheat Sheet

Bu cheat sheet, Python'da dict'lerle çalışırken yaygın kullanılan metotların özetini verir.

- **get()**
  - Belirtilen anahtara sahip değeri döndürür. Anahtar bulunamazsa hata verir veya varsayılan bir değer(varsa) döndürür. Varsayılan değer, belirtilen anahtarın ardından virgülle ayrılmış şekilde yazılır.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    car.get("brand")
    # "Pego" 
    car.get("age", "bilgi bulunamadi")
    # "bilgi bulunamadi"
    ```

- **pop()**
  - Bir anahtar belirtilerek bu anahtar-değer çifti sözlükten silinir. Methodun dönüş değeri, silinen anahtarın değeridir ve istenirse bir değişkene atanabilir. Eğer belirtilen anahtar bulunamazsa, hata alınır veya varsayılan bir değer (varsa) döndürür. Varsayılan değer, belirtilen anahtarın ardından virgülle ayrılmış şekilde yazılır.

  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    popped_value = car.pop("brand")
    # popped_value = "Pego"
    car.pop("age", "bilgi bulunamadi")
    # "bilgi bulunamadi"
    ```

- **popitem()**
  - Bir sözlüğün son anahtar değer çiftini kaldırır. Tuple şeklinde oluşan bu çift kullanılmak istenirse bir değişkene atanabilir. Eğer sözlük boşsa, hata alınır.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    popped_pair = car.popitem()
    # popped_pair = ("price", 100)
    ```

- **keys()**
  - Bir sözlükteki tüm anahtarları döndürür. `list()` kullanılarak liste şeklinde ulaşılır.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    keys = list(car.keys())
    # keys = ["brand", "model", "stock", "price"]
    ```

- **values()**
  - Bir sözlükteki tüm değerleri döndürür, `list()` kullanılarak liste şeklinde ulaşılır.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    values = list(car.values())
    # values = ["Pego", "3008", 3, 100] 
    ```

- **items()**
  - Bir sözlükteki anahtar-değer tuple çiftlerini döndürür. `list()` kullanılarak liste şeklinde ulaşılır.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    items = list(car.items())
    # values = [('brand', 'Pego'), ('model', '3008'), ('stock', 3), ('price', 100)]
    ```

- **clear()**
  - Bir sözlükteki tüm anahtar-değer çiftlerini temizler.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    car.clear()
    # {}
    ```

- **update()**
  - Bir sözlüğü başka bir sözlükle günceller. Eğer güncellenen sözlükte aynı anahtar varsa, bu anahtarın değeri güncellenir aksi halde yeni bir anahtar-değer çifti eklenir.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    car.update({"brand": "Reno"})
    # car = {"brand": "Reno", "model": "3008", "stock": 3, "price": 100,}
    colors = {
    "color": "White"
    }
    car.update(colors)
    # car = {"brand": "Reno", "model": "3008", "stock": 3, "price": 100, "color": "White", }
    ```

## BONUS 
 
- **fromkeys()**
  - Belirtilen anahtar listesinden yeni bir sözlük oluşturur. Her anahtar, başlangıçta belirtilen tek-bir- değere sahip olur. Varsayılan değer belirtilmezse, anahtarların değeri None olur.
  - Örnek:
    ```python
    keys = ("brand", "model", "stock") # ya da keys = ["brand", "model", "stock"]
    car = dict.fromkeys(keys)
    # car = {"brand": "None", "model": "None", "stock": "None",}
    default_value = "değer"
    car = dict.fromkeys(keys, default_value)
    # car = {"brand": "değer", "model": "değer", "stock": "değer",}
    ```
    
- **setdefault()**
  - Belirtilen anahtar sözlükte aranır ve bulunursa, değerini döndürür. Anahtar tek yazılabileceği gibi anahtar-değer çifti birlikte de yazılabilir. Anahtar sözlükte bulunamazsa çifti sözlüğe ekler, ve değeri döndürür. Değer girilmemişse belirtilen çift değeri None olarak sözlükte yer alır ve None döndürür.
  - Örnek:
    ```python
    car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,}
    car.setdefault("brand")
    # "Pego"
    car.setdefault("color","white")
    # "white"
    # car = {"brand": "Pego", "model": "3008", "stock": 3, "price": 100, "color": "white", }
    ```