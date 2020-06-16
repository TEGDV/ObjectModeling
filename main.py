class Character():
    def __init__(self, name,type_, gender, atack):
        self.name = name
        self.type_ = type_
        self.gender = gender
        self.atack = atack

    def greet(self):
        print('Hi my name is {} and Im a {} {}, nice to meet you'.format(self.name,self.gender,self.type_))

    def atack(self):
        print('the {} named {} atack with {} '.format(self.type_,self.name,self.atack))


if __name__ == "__main__":
    print('>>>>> Welcome to the creation menu <<<<<')
    option = input('to continue press anykey or write "No" then press enter to exit')

    if option == 'No':
        print('Thanks for use this software')

