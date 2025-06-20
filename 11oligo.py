# 11oligo.py by Kassidy

def tm(A, C, G, T):
    nt_count = A + C + G + T                         # count total
    if nt_count <= 13: return (A + T)*2 + (G + C)*4  # use formula 1
    else: return 64.9 + 41*(G + C - 16.4) / nt_count # use formula 2

print(tm(5, 7, 3, 4))
print(tm(1, 0, 4, 5))