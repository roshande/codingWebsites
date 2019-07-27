input1 = raw_input().split(' ')
trans = int(input1[0])
curr_bal = float(input1[1])
#trans,curr_bal = map(float,(raw_input().split(' ')))
if int(trans) %5 != 0 or (trans + 0.5) > curr_bal or trans == 0:
    print("%.2f"%curr_bal)
else:
    new_bal = curr_bal - trans - 0.5
    print("%.2f"%new_bal)
