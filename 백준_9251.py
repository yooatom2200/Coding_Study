# LCS(Longest Common Subsequence)
# 단어 알파벳 하나씩 비교
# 같으면 LCS[i-1][j-1] + 1 값 저장
# 다르면 LCS[i-1][j] 나 LCS[i][j-1]중 큰 값 저장

s1 = input()
s2 = input()

i = len(s1) + 1
j = len(s2) + 1

LCS = [[0] * j] * i

