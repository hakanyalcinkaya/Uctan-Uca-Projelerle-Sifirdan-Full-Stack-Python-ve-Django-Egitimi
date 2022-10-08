# test skoru rakamsal bilgi icermelidir
# test skoru 0 ila 100 arasinda olmalidir
# test skoru 45 alti ise kaldi
# test skoru 45 ve uzeri ise gecer
# test skoru 55 ve uzeri ise orta
# test skoru 75 ve uzeri ise iyi
# test skoru 85 ve uzeri ise pekiyi


test_score = input("Test Skorunu Giriniz: ")
result = ""

if not test_score.isnumeric():
    print("Lutfen Rakamsal Bilgi Giriniz")
elif 0 <= int(test_score) <= 100:
    test_score = int(test_score)
    if test_score >= 85:        
        result = "pekiyi"
    elif test_score >= 75:
        result = "iyi"
    elif test_score >= 55:
        result = "orta"
    elif test_score >= 45:
        result = "gecer"
    else:
        result = "kaldi"
else:
    print("lutfen 0 ila 100 arasinda bilgi giriniz")

print(result)