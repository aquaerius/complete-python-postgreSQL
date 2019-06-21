from create_exceptions import MyGoodError

def login(integer):
    if type(integer) != type(int):
        raise MyGoodError
    else:
        print(int(integer))


try:
    login('Whassa')
except Exception:
    pass



