class Dog:
    name='unknown'

    def __init__(self, breed, speed):
        self.is_walked = False
        self.speed = speed
        self.breed = breed
        self.tricks = []

    def walk(self):
        print(f'dog {self.name} walks')
        self.is_walked = True

    def learn_trick(self, trick):
        self.trick += [trick]

class DogSpike(Dog):
    name = 'Spike'

    def run(self):
        print(f'dog {self.name} is running {self.speed} km/h')

class DogMike(Dog):
    name = 'Mike'   

my_dog = DogSpike('bulldog', 12)    
friends_dog = DogMike('pitbull', 20)

print(f'my dog name is {my_dog.name}')
print(f'friend speed is {my_dog.speed} km/h')
print(f'my friend\'s dog name is {friends_dog.name}')
print(f'friend\'s dog speed is {friend_dog.speed} km/h')
my_dog.run

