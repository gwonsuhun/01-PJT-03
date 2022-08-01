import sys


number = int(input())
for i in range(1,number+1):
    A,B,C  = map(int,(input().split()))
    if A == B:
        print(f"#{i} {C}")
    elif A == C:
        print(f"#{i} {B}")
    elif B == C:
        print(f"#{i} {A}")

# 직사각형의 3개의 길이를 알려줘서  3개중 다른 1개의 길이가 구하고 싶은 길이랑 같다.
sys.stdin = open("_직사각형길이찾기.txt")
