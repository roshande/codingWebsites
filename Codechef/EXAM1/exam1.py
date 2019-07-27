def calculate_marks(correct, attempt):
    marks, n = 0, len(correct)
    wrong = False
    for i in range(n):
        if wrong:
            wrong = False
            continue
        if attempt[i] == 'N':
            continue
        if attempt[i] != correct[i]:
            wrong = True
        else: #elif attempt[i] == correct[i]:
            marks += 1
    return marks

for _ in range(int(input())):
    q = int(input())
    correct = input()
    attempt = input()
    marks = calculate_marks(correct, attempt)
    print(marks)
