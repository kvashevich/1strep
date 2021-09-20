while True:
    counter = input("enter word --> ")
    if counter == 'stop':
        break
    print(counter.replace('a', 'b', 3))


spisokone = ['awdawd', 'python', '123', '2021', 'ukraina']
for i in range(0, len(spisokone)):
    spisokone[i] = spisokone[i].replace(spisokone[i], 'word')
print(spisokone)
