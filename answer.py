N, X = map(int, input().split())
A_vec = list(map(int, input().split()))

for A in A_vec:
    if A < X:
        print(1)
        X = A
    else:
        print(0)
