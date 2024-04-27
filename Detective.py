import random


def bool_search(lst, Ts, Fs):
    for i in range(len(lst)):
        if lst[i] == True:
            Ts.append(f"{lst}[{i}]")
        else:
            Fs.append(f"{lst}[{i}]")


def show_all_statments(allStatments):
    for i in allStatments:
        for j in i:
            if i[j]:
                print(j, ": ", True)
            else:
                print(j, ": ", False)


def detective_result(Decisive_statments):
    for i in Decisive_statments:
        for j in i:
            if i[j]:
                yield j


A = [None, None, None]
B = [None, None, None]
C = [None, None, None]
D = [None, None, None]

# I used list variables as counter because they are refrence type and will be changed after we pass them to functions
trues = []
falses = []
while not ((len(trues) == 6) and (len(falses) == 6)):

    trues = []
    falses = []

    # A[1] is a key statment and can help us to reach to answer faster
    A[0], A[1] = random.choice([True, False]), random.choice([True, False])
    A[2] = True  # Assumption of the problem

    B[0], B[1] = random.choice([True, False]), random.choice([True, False])
    B[2] = not (A[1])
    C[1] = B[2]
    D[2] = not (B[1])
    D[0] = not (B[0])
    C[0] = not A[0]
    C[2] = random.choice([True, False])
    D[1] = not (C[2])

    # Now we check condition of A[1]
    if A[1]:
        B[0], B[1] = True, True
        C[1], D[0], D[2] = False, False, False

    for i in [A, B, C, D]:
        bool_search(i, trues, falses)


A_statments = [{"A and C meet each other": A[0]}, {"B is the criminal": A[1]},
               {"Thief didn't know that car is for the detective": A[2]}]

B_statments = [{"D is not guilty": B[0]}, {
    "A is not criminal": B[1]}, {"B is not guilty": B[2]}]

C_statments = [{"A and C never meet each other": C[0]}, {
    "B is not guilty": C[1]}, {"D can drive": C[2]}]

D_statments = [{"D is guilty": D[0]}, {
    "D can't drive": D[1]}, {"A is guilty": D[2]}]


"""
these lines below is to show the truthiness of all of statments
"""
# allStatments = [*A_statments, *B_statments, *C_statments, *D_statments]
# show_all_statments(allStatments)


# -----------------------show result-----------------------
# Truthiness of these statments can lead us to the criminal
decisive_statments = [A_statments[1], B_statments[1],
                      C_statments[1], D_statments[0], D_statments[2]]
result = list(detective_result(decisive_statments))  
for i in result:
    print(i)
