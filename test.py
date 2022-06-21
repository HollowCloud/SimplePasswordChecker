class Passed():
    def __init__(self, password):
        self._password = password
    
    def output(self):
        print(f'Your password is {self._password}')

p = input('Enter password: ')
print()
passed = Passed(p)
passed.output()