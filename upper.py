spisokone = ['jaVa dAa aFFda dKKdw', 'PdTwON pytho pYthOn', 'w12AWdw 122Aq', 'ad231 AAAAw']
for i in range(0, len(spisokone)):
    spisokone[i] = spisokone[i].upper()
print(spisokone)

while True:
    edit1 = input('enter text: ')
    if edit1 == 'stop':
        print('end')
        break
    print(edit1.upper())