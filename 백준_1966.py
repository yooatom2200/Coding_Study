count = int(input())
for _ in range(count):
    note_count, note = map(int, input().split())
    notes = list(map(int, input().split()))
    notes_index = []
    seq = 0

    for i in range(len(notes)):
        notes_index.append(i)

    while notes:
        if notes[0] == max(notes):
            seq += 1
            if notes_index[0] == note:
                print(seq)
                break
            
            notes.pop(0)
            notes_index.pop(0)
        else:
            notes.append(notes.pop(0))
            notes_index.append(notes_index.pop(0))
