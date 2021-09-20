while True:
    strokaed = input('stroka dlya razdeleniya: ')
    if strokaed  == 'stop':
        print('end')
        break
    simvol = input('simvol razdeleniya: ')
    if simvol  == 'stop':
        print('end')
        break

    print(strokaed.split(simvol))

spisokone = ['awdawd.python,fhtfhtf.trrhf', '123.fwew.fwwfe', '.2021', '.ukraina.']
for i in range(0, len(spisokone)):
    spisokone[i] = spisokone[i].split('.')
print(spisokone)

