import re

try:
    fhand = open("C:/Users/scott/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/mbox.txt")
except FileNotFoundError:
    print("파일 못 찾음")

numStringList = []
for line in fhand:
    line = line.rstrip()
    if re.findall('^New Revision: ', line):
        numStringList.append(int(line[14:]))

print(f"Total {len(numStringList)} lines are matched")
print("Average : ", sum(numStringList)/len(numStringList))  
