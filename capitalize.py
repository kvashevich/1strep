spisokone = ['jaVa daa', 'PYTHON', 'w12', 'ad231 daw']
for i in range(0, len(spisokone)):
    spisokone[i] = spisokone[i].capitalize()
print(spisokone)

while True:
    edit1 = input('enter word: ')
    if edit1 == 'stop':
        print('end')
        break
    print(edit1.capitalize())
