prevFile = open('allmember.txt') #modify to your file name
currFile = open('allMember2019-06-15 00.txt')
preSet=set()
curSet=set()
for line in open('allmember.txt'):
    line=prevFile.readline()
    preSet.add(line)
for line in open('allMember2019-06-15 00.txt'):
    line=currFile.readline()
    curSet.add(line)

print("离开成员：")
print(preSet-curSet)
print("新增成员:")
print(curSet-preSet)
