# %%
import sys
import os

# ローカルに input.txt があれば、input 関数自体をファイル読み込み用に作り変える
if os.path.exists('input.txt'):
    _f = open('input.txt', 'r')
    def input():
        line = _f.readline()
        if not line: # EOF（ファイルの終端）に達した場合
            raise EOFError
        return line.rstrip('\r\n')
    
    # 念のため sys.stdin も差し替えておくと、sys.stdin.read() 等にも対応できます
    sys.stdin = _f

#ここから回答を記載
#%%
N = int(input())
qrs = [list(map(int, input().split())) for _ in range(N)]
Q= int(input())
tds = [list(map(int, input().split())) for _ in range(Q)]
# %%
for td in tds:
    t, d = td

    k = ((d - qrs[t-1][1]-1) // qrs[t-1][0]) + 1

    print(qrs[t-1][1] + k * qrs[t-1][0])
# %%
