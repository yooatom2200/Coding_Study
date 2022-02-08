count = int(input())
seq = 0
for _ in range(count):
    note_count, note = map(int, input().split())
    notes = list(map(int, input().split()))
    if notes[0] == max(notes):
