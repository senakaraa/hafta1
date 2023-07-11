from collections import Counter

text = input("Enter text")


lst =Counter(text.lower()).most_common()
#küçült,say,çok olanı bul,listele
if lst:
    themost= lst[0][1]
    common = [char for char, count in lst if count == themost]
    #yaygın olanlardan ayrı liste yap
    print("more repeatings:")

    for char in common:
        if char==" ":
            continue
        else:
            print(f"{char}: {themost} kez")

else:
    print("Metinde herhangi bir karakter bulunamadı.")