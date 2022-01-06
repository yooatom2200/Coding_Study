# LCS(Longest Common Subsequence)
# 단어 알파벳 하나씩 비교
# 같으면 LCS[i-1][j-1] + 1 값 저장
# 다르면 LCS[i-1][j] 나 LCS[i][j-1]중 큰 값 저장

s1 = input()
s2 = input()

si = len(s1) + 1
sj = len(s2) + 1

LCS = [[0] * sj] * si

for i in range(si):
    for j in range(sj):
        if i == 0 or j == 0:
            continue
        elif s1[i-1] == s2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        elif s1[i-1] != s2[j-1]:
            LCS[i][j] = LCS[i-1][j] if LCS[i-1][j] >= LCS[i][j-1] else LCS[i][j-1]

print(max(max(LCS)))
