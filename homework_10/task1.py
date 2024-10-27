def vowel(text):
    count = 0
    for i in range(len(text)):
        if text[i].lower() in ["a","e","i","o","u"]:
            count += 1
    print(count)

vowel("gaga")
vowel("gAgA")