alphabet = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
number = int(input('введите промежуток')) # в моем коде 32 максимум, >32 = "string index out of range"
code = str(input('текст, который хотим закодировать'))
for i in range(len(code)):
    for j in range(len(alphabet)):
        if code[i] == alphabet[j]:
            j += number + number
            if j > 63:
                j = j - 64
                print(alphabet[j], end = '')
            else:
                print(alphabet[j], end = '')
    else:
        if code[i] not in alphabet:
            print(code[i], end='',)