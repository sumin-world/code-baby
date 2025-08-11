s = str(input())

alphabet = []

# 'a'의 아스키 코드부터 'z'의 아스키 코드까지 반복
for i in range(ord('a'), ord('z') + 1):
    # 아스키 코드 값을 다시 문자로 변환하여 리스트에 추가
    alphabet.append(chr(i))

result = []
for char in alphabet:
    count = s.count(char)
    result.append(str(count))