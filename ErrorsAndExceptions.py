#Write a function that has error handling and accepts only integers:
def test():
    while True:
        try:
            mv = int(input('Please enter a number: '))
        except ValueError as e:
            print('An error has occurred : {}'.format(e))
            continue
        else:
            print('--------------------------------')
            print('The provided number square is : {}'.format(mv**2))
            break

test()


#Some for loop error handling example:
def some_for_loop():

        try:
            for i in ['a', 'b', 'c']:
                print(i**2)
        except TypeError as e:
            print()
            print('Watch out for error : {}'.format(e))
        finally:
            print('The issue has been fixed')
            print()
some_for_loop()


#Write a function that has error handling:
def test_error():
    x = 5
    y = 0
    try:
        z = x/y
    except ZeroDivisionError as e:
        print('An error has occurred : {}'.format(e))
        print(f'Any number divided by {y} is not defined.')
    finally:
        print('All done')

test_error()