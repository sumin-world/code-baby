// 1. 문자열 연산과 반복문 사용
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=' ')

alphabet = []
# 'a'의 아스키 코드부터 'z'의 아스키 코드까지 반복
for i in range(ord('a'), ord('z') + 1):
    # 아스키 코드 값을 다시 문자로 변환하여 리스트에 추가
    alphabet.append(chr(i))

# 백준 10808 - 알파벳 개수
s = input()

# 1단계: a부터 z까지 알파벳 만들기
alphabet = []
for i in range(26):
    letter = chr(ord('a') + i)  # 'a', 'b', 'c', ... 'z'
    alphabet.append(letter)

# 2단계: 각 알파벳의 개수 세기
result = []
for char in alphabet:
    count = s.count(char)
    result.append(str(count))

# 3단계: 결과 출력
print(' '.join(result))