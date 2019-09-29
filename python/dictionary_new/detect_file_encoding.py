import chardet

files = [
    'vocabulary.txt',
    '历史.txt',
    '地理.txt',
]

for txt_file in files:
    print(txt_file)
    f = open(txt_file, 'rb')
    data = f.read()
    print(chardet.detect(data))
