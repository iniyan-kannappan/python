while True:
    try:
        print('Type in a integer.')
        integer=(int(input()))
        break
    except ValueError:
        print('Please type in a integer value.')
