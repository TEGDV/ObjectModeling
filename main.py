class Character():
    def __init__(self, name,type_, gender, atack):
        self.name = name
        self.type_ = type_
        self.gender = gender
        self.atack = atack

    def greeting(self):
        print('Hi my name is {} and Im a {} {}, nice to meet you'.format(self.name,self.gender,self.type_))

    def do_atack(self):
        print('the {} named {} atack with {} '.format(self.type_,self.name,self.atack))


if __name__ == "__main__":
    print('>>>>> Welcome to the creation menu <<<<<')
    option = input('to continue press anykey or write "No" then press enter to exit   ')

    if option == 'no':
        print('Thanks for use this software')
    else:
        newChar = Character(input('Write the character name:  '), input('Write the type the type of your character example warrior, elf, ranger, thief, etc  '), input('Write your character gender:   '),input('Name your character attack:  '))
 
        while option != 'no':
            print('this is the character menu what do you want that {} do?'.format(newChar.name))
            print('')
            print('1:  Greet')
            print('2:  Atack')
            print('3:  Exit')
            print('')

            option2 = input('Select your option:   ')
            print('')

            if option2 == '1':
                newChar.greeting()
            if option2 == '2':
                newChar.do_atack()
            if option2 == '3':
                option = 'no'


