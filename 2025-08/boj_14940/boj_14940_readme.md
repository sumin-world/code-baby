# BOJ 14940 — 쉬운 최단거리

- **분류**: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프
- **난이도**: Silver I
- **입력**: n×m 지도, 0(갈 수 없는 땅), 1(갈 수 있는 땅), 2(목표지점)
- **출력**: 각 지점에서 목표지점까지의 최단거리

---

## 문제 요약

지도가 주어졌을 때, 모든 지점에서 목표지점(2)까지의 최단거리를 구하는 문제입니다.
- 오직 **가로와 세로**로만 이동 가능 (대각선 이동 불가)
- 목표지점은 **단 하나**만 존재

---

## 알고리즘 아이디어

### 핵심: BFS (너비 우선 탐색)
1. **목표지점(2)을 시작점**으로 BFS 수행
2. **거리 0부터 시작**하여 인접한 갈 수 있는 땅(1)으로 확산
3. **동시에 같은 거리의 모든 점들을 탐색** → 최단거리 보장

### 왜 BFS인가?
- **가중치가 모두 1**인 최단경로 문제 → BFS가 최적
- **한 번의 탐색**으로 모든 지점의 최단거리 계산 가능
- 시간복잡도: O(N×M)

---

## 복잡도

- **시간 복잡도**: O(N×M) - 각 칸을 최대 한 번씩 방문
- **공간 복잡도**: O(N×M) - 거리 배열 + BFS 큐

---

## 구현 포인트 / 함정

### 1. 출력 조건 주의
- **갈 수 없는 땅 (0)** → `0` 출력
- **갈 수 있지만 도달 불가능한 땅** → `-1` 출력  
- **목표지점** → `0` 출력

### 2. 초기화 전략
```python
# 모든 갈 수 있는 땅을 -1로 초기화
# 갈 수 없는 땅은 0으로 초기화
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            distance[i][j] = 0    # 갈 수 없는 땅
        else:
            distance[i][j] = -1   # 갈 수 있는 땅 (아직 미방문)
```

### 3. BFS 방향 벡터
```python
# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
```

### 4. 경계 체크
```python
if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
    # 범위 내 + 아직 방문하지 않은 갈 수 있는 땅
```

---

## 예제 분석

### 입력 해석
```
15 15                    # 15×15 지도
2 1 1 1 1 ...           # 첫 줄: 목표지점(2)이 (0,0)에 위치
1 1 1 1 1 ...           # 나머지: 대부분 갈 수 있는 땅(1)
...
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1   # 중간에 갈 수 없는 땅(0) 존재
```

### 출력 해석
- **(0,0)** 목표지점 → `0`
- **(0,1)** → 목표지점에서 거리 `1`  
- **(0,2)** → 목표지점에서 거리 `2`
- **갈 수 없는 땅** → `0`
- **도달 불가능한 영역** → `-1` (예제에서는 모든 땅이 연결됨)

---

## 알고리즘 단계

1. **입력 처리**: 지도 읽기, 목표지점 찾기
2. **거리 배열 초기화**: 갈 수 없는 땅은 0, 갈 수 있는 땅은 -1
3. **BFS 시작**: 목표지점을 시작점으로 큐에 삽입, 거리 0으로 설정
4. **BFS 탐색**: 
   - 큐에서 현재 위치 꺼내기
   - 상하좌우 4방향 탐색
   - 갈 수 있고 아직 방문하지 않은 땅이면 큐에 추가
   - 거리는 현재 거리 + 1
5. **결과 출력**: 거리 배열 출력

---

# 📘 Python 문법 정리 (BOJ 14940 — 쉬운 최단거리)

## 1. 2차원 리스트 입력

```python
n, m = map(int, input().split())

# 방법 1: 한 줄씩 읽기
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 방법 2: 리스트 컴프리헨션 
grid = [list(map(int, input().split())) for _ in range(n)]
```

## 2. 2차원 리스트 초기화

```python
# n×m 크기의 2차원 배열을 -1로 초기화
distance = [[-1] * m for _ in range(n)]

# 주의: distance = [[-1] * m] * n  # 잘못된 방법!
# 이렇게 하면 모든 행이 같은 리스트를 참조함
```

## 3. 목표지점 찾기

```python
target_row, target_col = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            target_row, target_col = i, j
            break
    if target_row != -1:  # 찾았으면 외부 반복문도 종료
        break
```

## 4. BFS 구현

```python
from collections import deque

# BFS 초기화
queue = deque([(target_row, target_col)])
distance[target_row][target_col] = 0

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 경계 체크 + 방문 체크 + 갈 수 있는 땅 체크
        if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and grid[nx][ny] == 1:
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))
```

## 5. 결과 출력

```python
# 2차원 배열 출력
for row in distance:
    print(*row)  # 언패킹으로 공백 구분하여 출력
    
# 또는
for i in range(n):
    for j in range(m):
        print(distance[i][j], end=' ' if j < m-1 else '\n')
```

## 6. deque 사용법

```python
from collections import deque

queue = deque()
queue.append((x, y))        # 뒤에 추가
x, y = queue.popleft()      # 앞에서 제거
```

📌 **deque vs list**
- `deque.popleft()`: O(1)
- `list.pop(0)`: O(N) - 비효율적!

## ✅ 핵심 Python 문법 요약

1. **2차원 리스트** → `[[-1] * m for _ in range(n)]`
2. **deque 활용** → `from collections import deque`
3. **BFS 패턴** → `queue.append()`, `queue.popleft()`
4. **방향 벡터** → `dx = [-1, 1, 0, 0]`, `dy = [0, 0, -1, 1]`
5. **경계 체크** → `0 <= nx < n and 0 <= ny < m`
6. **출력 최적화** → `print(*row)` 언패킹

---

## 🔍 디버깅 팁

### 흔한 실수들
1. **2차원 배열 초기화 실수**: `[[-1] * m] * n` 사용 금지
2. **BFS 큐 구현**: `list.pop(0)` 대신 `deque.popleft()` 사용
3. **방문 체크**: `distance[nx][ny] == -1` 조건 확인
4. **출력 조건**: 갈 수 없는 땅(0), 도달 불가능(-1) 구분

### 테스트 케이스 만들기
```python
# 간단한 테스트 케이스
3 3
0 1 0
1 2 1
0 1 0

# 예상 출력
0 1 0
1 0 1  
0 1 0
```