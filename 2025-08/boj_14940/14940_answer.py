import sys
input = sys.stdin.readline

n = int(input())
stack = []
out_lines = []

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        out_lines.append(str(stack.pop() if stack else -1))
    elif cmd[0] == "size":
        out_lines.append(str(len(stack)))
    elif cmd[0] == "empty":
        out_lines.append("0" if stack else "1")
    elif cmd[0] == "top":
        out_lines.append(str(stack[-1] if stack else -1))

sys.stdout.write("\n".join(out_lines))
