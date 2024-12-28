def translate(string):
    result = []
    for bracket in string:
        if bracket == "(":
            result.append(1)
        else:
            result.append(-1)
    return result


def tree(bracketing, right=False):
    total = 0
    i = 0
    if right and len(bracketing) == 0:
        print("R", end="", sep="")
    elif not right and len(bracketing) == 0:
        print("L", end="", sep="")
    else:
        while i < len(bracketing):
            total += bracketing[i]
            if total == 0:
                return tree(bracketing[1:i]), tree(bracketing[i + 1 :], right=True)
            i += 1


bracketings = input()
tree(translate(bracketings))