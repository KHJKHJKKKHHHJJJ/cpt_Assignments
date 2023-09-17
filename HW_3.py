import re
try:
    fhand = open('C:/Users/scott/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/mbox.txt')
except FileNotFoundError:
    print("파일 주소를 확인하세요")
user_req = input("텍스트를 입력하세요: ").split(' ')
count = 0
foundList = []
for line in fhand:
    line = line.rstrip()
    adresses = re.findall("[a-zA-Z0-9]\S+@[a-zA-Z0-9.]+[a-zA-Z]", line)
    for adress in adresses:
        for email in user_req:
            if email == adress:
                if email not in foundList:
                    if len(foundList) == 0:
                        print('추출된 이메일 주소: ')
                    foundList.append(email)
                    print(email)
                    count += 1 

if count == 0:
    print("이메일 주소가 발견되지 않았습니다.")
