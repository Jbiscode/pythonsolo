python = 'Python is amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace('python',"Java"))

index = python.index('n')
print(index)
index = python.index('n',index + 1)
print(index)

print(python.find('java'))       # find를 쓰면 없으면 -1 뜨고 그대로 진행
# print(python.index('java'))
print('hi')