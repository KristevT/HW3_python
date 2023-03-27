word = input()
if word.find('f') != -1 and word.find('f') == word.rfind('f'):
    print(word.find('f'))
elif word.find('f') != word.rfind('f'):
    print(word.find('f'), word.rfind('f'))