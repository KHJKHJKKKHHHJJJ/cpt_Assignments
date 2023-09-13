'''
재귀 호출 방식으로 입력 문자열의 순서를 거꾸로 뒤집는 함수 rev_str(str)을
 완성하고 다음 문자열을 거꾸로 뒤집는 프로그램을 작성하라. 아래의 주어진 코드를 부분적으로 활용하라. (25점)
'''
def rev_str(str, new_str = ''):
    left_word = len(str)
    if left_word == 0:
        return new_str
    new_str += str[left_word-1]
    str = str[:left_word-1]
    return rev_str(str, new_str)

if __name__ == '__main__':

    print(rev_str('ABCDE'))

    print(rev_str('Come again, Forever young!'))

    print(rev_str('Amore, Roma'))

