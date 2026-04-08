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
