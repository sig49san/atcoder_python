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

#%%
N = int(input())
LRs = [list(map(int, input().split())) for _ in range(N)]
    
# %%
saitei = 0
saikou = 0
for L, R in LRs:
    saitei += L
    saikou += R

if saitei > 0 or saikou < 0:
    print("No")
    exit()

#%%
print("Yes")
ans = [LR[0] for LR in LRs]
sum_ans= sum(ans)
for i in range(N):
    if sum_ans < 0:
        ans[i] += min(LRs[i][1] - LRs[i][0], -sum_ans)
        sum_ans += min(LRs[i][1] - LRs[i][0], -sum_ans)
    else:
        break
    
print(*ans)
# %%
