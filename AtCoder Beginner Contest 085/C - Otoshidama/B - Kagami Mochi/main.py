N = int(input())
s = [int(input()) for i in range(N)]

print(len(dict.fromkeys(s)))
