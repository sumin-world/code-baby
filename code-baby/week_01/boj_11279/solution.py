import heapq
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 연산의 개수 N 입력받기
n = int(input())

# 힙으로 사용할 빈 리스트 생성
heap = []

for _ in range(n):
    x = int(input())

    if x > 0:
        # x가 자연수이면, 최대 힙으로 사용하기 위해 부호를 바꿔서 힙에 추가
        heapq.heappush(heap, -x)
    else: # x가 0이면
        # 힙이 비어있지 않은 경우
        if heap:
            # 가장 작은 값(원래는 가장 컸던 값의 음수)을 꺼내서
            # 다시 부호를 바꿔 원래의 최댓값으로 만들어 출력
            print(-heapq.heappop(heap))
        # 힙이 비어있는 경우
        else:
            print(0)