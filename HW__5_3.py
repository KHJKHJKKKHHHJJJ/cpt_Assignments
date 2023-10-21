from collections import Counter

file1 = open("C:/Users/scott/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/06 file01.txt").readlines()
file2 = open("C:/Users/scott/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/06 file02.txt").readlines()

lifile1 = []
lifile2 = []

for words in file1:
    words = words.replace(".","").lower().rstrip()
    for word in words.split():
        lifile1.append(word)

for words in file2:
    words = words.replace(".","").lower().rstrip()
    for word in words.split():
        lifile2.append(word)

result = Counter(lifile1) & Counter(lifile2)

for words in result:
    print(f"{words}: 파일1-{Counter(lifile1)[words]}, 파일2-{Counter(lifile2)[words]}")
