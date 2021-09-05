spisokone = ['jaVa daa adwda daadw', 'PYTHON pytho pYthon', 'w12adw 122wq', 'ad231 daw']
for i in range(0, len(spisokone)):
    spisokone[i] = spisokone[i].title()
print(spisokone)

while True:
    edit1 = input('enter text: ')
    if edit1 == 'stop':
        print('end')
        break
    print(edit1.title())
