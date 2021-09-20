spisok1 = [['awdawd', 'python,fhtfhtf', 'trrhf'], ['123', 'fwew', 'fwwfe'], ['', '2021'], ['', 'ukraina', '']]
counter = 0
while counter < len(spisok1):
    spisok1[counter] = '.'.join(spisok1[counter])
    counter += 1
print(spisok1)


spisokone = [['awdawd', 'python,fhtfhtf', 'trrhf'], ['123', 'fwew', 'fwwfe'], ['', '2021'], ['', 'ukraina', '']]
for i in range(0, len(spisokone)):
    spisokone[i] = '.'.join(spisokone[i])
print(spisokone)

