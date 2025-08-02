#!/bin/bash

# 📂 1주차 스터디 폴더 이름
WEEK_DIR="week01_2025-08-02_to_08-10"
REPO_DIR="code-baby"

# 폴더 구조 생성
mkdir -p "$REPO_DIR/$WEEK_DIR/boj_1927"
mkdir -p "$REPO_DIR/$WEEK_DIR/review"

# --- week01 README.md 생성 ---
cat > "$REPO_DIR/$WEEK_DIR/README.md" << EOF
# 1주차 스터디 (2025-08-02 ~ 2025-08-10)

## 진행 목표
- 백준 문제 풀이 & 리뷰
- 언어별 풀이 공유 (C, Rust, Python)
- 매일 최소 1문제 이상

---

## 문제 목록

| 번호 | 문제명 | 링크 | 상태 |
|------|--------|------|------|
| 1927 | 최소 힙 | [백준 1927](https://www.acmicpc.net/problem/1927) | ⬜ 진행중 |

---

## 👥 팀원 진행 상황

### sumin-world (C / Rust)
- [ ] C 풀이 완료
- [ ] Rust 풀이 완료
- [ ] 코드 리뷰

### silverkkang (Python)
- [ ] Python 풀이 완료
- [ ] 코드 리뷰

---

## 폴더 구조

week01_2025-08-02_to_08-10/
├── boj_1927/
│   ├── sumin-world_min_heap.c
│   ├── sumin-world_min_heap.rs
│   ├── silverkkang_min_heap.py
│   └── README.md
└── review/
    └── memo.md

---

## 리뷰 계획
- 코드 리뷰: 주말(8/9~8/10)에 상호 리뷰
- 성능 개선 / 다른 접근법 논의
EOF

# --- boj_1927 README.md 생성 ---
cat > "$REPO_DIR/$WEEK_DIR/boj_1927/README.md" << EOF
# 백준 1927 - 최소 힙

## 문제 설명
[백준 1927](https://www.acmicpc.net/problem/1927)

- 최소 힙을 이용하여 다음 연산을 수행하는 문제
1. 자연수 x를 입력하면 배열에 x 추가
2. 0을 입력하면 배열에서 가장 작은 값 출력 후 제거 (없으면 0 출력)

---

## 접근 방법
- 최소 힙 구현 (C: priority queue / Rust: BinaryHeap / Python: heapq)
- 입력이 많으므로 빠른 입출력 사용

---

## 진행 상황

| 팀원         | 언어    | 풀이 상태 |
|-------------|--------|---------|
| sumin-world | C      | ⬜ |
| sumin-world | Rust   | ⬜ |
| silverkkang | Python | ⬜ |

---

## 예제 입력
\`\`\`
9
0
12345678
1
2
0
0
0
0
32
\`\`\`

## 예제 출력
\`\`\`
0
1
2
12345678
0
\`\`\`
EOF

# --- 코드 파일 템플릿 생성 ---
touch "$REPO_DIR/$WEEK_DIR/boj_1927/sumin-world_min_heap.c"
touch "$REPO_DIR/$WEEK_DIR/boj_1927/sumin-world_min_heap.rs"
touch "$REPO_DIR/$WEEK_DIR/boj_1927/silverkkang_min_heap.py"
touch "$REPO_DIR/$WEEK_DIR/boj_1927/input.txt"
touch "$REPO_DIR/$WEEK_DIR/review/memo.md"

echo "✅ 1주차 스터디 폴더와 템플릿 생성 완료"
