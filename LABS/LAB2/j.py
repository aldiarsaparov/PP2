passw = set()

for _ in range(int(input())):
    s = input()
    if (
        sum(map(str.isupper, s))
        and sum(map(str.islower, s))
        and sum(map(str.isdigit, s))
    ):
        passw.add(s)

print(len(passw))
print("\n".join(sorted(passw)))