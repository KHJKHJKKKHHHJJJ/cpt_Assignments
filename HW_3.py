import re
user_req = input("텍스트를 입력하세요: ")
adresses = re.findall("[a-zA-Z0-9]\S+@[a-zA-Z0-9.]+[a-zA-Z]", user_req)
if len(adresses) == 0:
    print("이메일 주소가 발견되지 않았습니다.")
else:
    for adress in adresses:
        print(adress)
