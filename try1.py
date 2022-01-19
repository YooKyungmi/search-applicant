info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

count = 0
requ = query[4].replace("and", "").replace("  ", " ")
requ = requ.split(' ')
r_score = requ[4]
location = [4]
for i in range(3, -1, -1):
    if requ[i] == "-":
        location.append(i)
for j in location:
    del requ[j]
requ = " ".join(requ)


for i in range(len(info)):
    check = info[i].split(' ')
    if check[4] > r_score:
        for k in location:
            del check[k]
        check = " ".join(check)
        if check == requ:
            count += 1
print(count)
