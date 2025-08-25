# BOJ 10828 — 스택

- **분류**: 구현, 자료구조, 스택  
- **입력**: N(명령 수), 이어서 N개의 명령  
- **출력**: `pop / size / empty / top`가 나올 때마다 결과 한 줄

---

## 명령

- `push X` : 정수 X를 스택에 넣기
- `pop`    : 맨 위 정수 빼고 출력, 없으면 `-1`
- `size`   : 스택 크기 출력
- `empty`  : 비었으면 `1`, 아니면 `0`
- `top`    : 맨 위 정수 출력, 없으면 `-1`

---

## 알고리즘 아이디어

- 스택은 **후입선출(LIFO)** 구조 → **배열(동적배열)**의 **뒤**를 top으로 사용하면 모든 연산이 O(1)
- Python: list `append/pop()`  
- Rust: `Vec`의 `push/pop/last/is_empty/len` 활용

---

## 복잡도

- 각 명령 O(1), 총 O(N), 추가 메모리 O(N)

---

## 구현 포인트 / 함정

- **입출력 최적화** (특히 Rust): 표준 입력 전체를 읽고, 출력은 버퍼에 모았다가 한 번에 출력
- 빈 스택에서 `pop/top`은 **반드시 `-1`**
- 명령 파싱 시 공백 분리: `push`만 두 토큰

---

## 예시

### 입력
```
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```

### 출력
```
2
2
0
2
1
-1
0
1
-1
0
3
```

---

## 파일

- `python.py` — Python 풀이
- `rust.rs` — Rust 풀이

---

# 📘 Python 문법 정리 (BOJ 10828 — 스택)

## 1. 표준 입력

- 빠른 입력을 위해 `sys.stdin.readline` 사용  
- `input()`은 느리기 때문에 권장하지 않음

```python
import sys
input = sys.stdin.readline
```

## 2. 리스트 (스택 구현)

Python에서 스택은 `list`로 구현

```python
stack = []
stack.append(10)  # push
stack.append(20)

print(stack.pop())   # pop -> 20
print(len(stack))    # size -> 1
print(1 if not stack else 0)  # empty -> 0 (비어있지 않음)
print(stack[-1])     # top -> 10
```

📌 **특징**
- `append(x)` : 맨 뒤에 원소 추가 (O(1))
- `pop()` : 맨 뒤 원소 제거 후 반환 (O(1))
- `len(list)` : 크기 확인
- `list[-1]` : 마지막 원소 접근
- `not list` : 리스트가 비어있으면 True

## 3. 조건문 (if-elif-else)

문자열 비교를 통해 명령 처리

```python
cmd = ["push", "3"]

if cmd[0] == "push":
    stack.append(int(cmd[1]))
elif cmd[0] == "pop":
    print(stack.pop() if stack else -1)
```

## 4. 삼항 연산자

조건식 한 줄 표현

```python
print(stack.pop() if stack else -1)
print(0 if stack else 1)
print(stack[-1] if stack else -1)
```

## 5. 문자열 처리

- `split()` : 공백 기준 분리

```python
cmd = "push 3".split()  # ["push", "3"]
```

## 6. 반복문

- `for _ in range(n):` : n번 반복 (인덱스 필요 없을 때 `_` 사용)

```python
n = int(input())
for _ in range(n):
    cmd = input().split()
    # 명령 처리
```

## ✅ 핵심 Python 문법 요약

1. **빠른 입력** → `sys.stdin.readline`
2. **리스트 메서드** → `append`, `pop`, `len`, `[-1]`, `not`
3. **조건문 / 삼항 연산자** → `if-elif-else`, `A if cond else B`
4. **문자열 처리** → `split()`
5. **반복문** → `for _ in range(n):`

---

## 📁 파일 구조

```
week02/10828/
├── README.md
├── python.py     # Python 솔루션
└── rust.rs       # Rust 솔루션
```

## 🔗 관련 문제

- BOJ 9012 - 괄호
- BOJ 10773 - 제로
- BOJ 1874 - 스택 수열