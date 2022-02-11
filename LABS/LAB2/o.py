def change2(s):
    s = s.replace("1", "ONE")
    s = s.replace("2", "TWO")
    s = s.replace("3", "THR")
    s = s.replace("4", "FOU")
    s = s.replace("5", "FIV")
    s = s.replace("6", "SIX")
    s = s.replace("7", "SEV")
    s = s.replace("8", "EIG")
    s = s.replace("9", "NIN")
    s = s.replace("0", "ZER")

    return s


def change1(s):
    s = s.replace("ONE", "1")
    s = s.replace("TWO", "2")
    s = s.replace("THR", "3")
    s = s.replace("FOU", "4")
    s = s.replace("FIV", "5")
    s = s.replace("SIX", "6")
    s = s.replace("SEV", "7")
    s = s.replace("EIG", "8")
    s = s.replace("NIN", "9")
    s = s.replace("ZER", "0")

    return s


s = input()

ans = str(eval(change1(s)))

print(change2(ans))