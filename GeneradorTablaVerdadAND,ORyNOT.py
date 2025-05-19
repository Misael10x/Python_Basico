valores = [0, 1]

print(" A | B | A AND B | A OR B | NOT A ")
print("-------------------------------")
for a in valores:
    for b in valores:
        and_op = a & b
        or_op = a | b
        not_a = int(not a)
        print(f" {a} | {b} |    {and_op}     |   {or_op}   |   {not_a} ")
