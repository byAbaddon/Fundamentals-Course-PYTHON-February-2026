class Parking:
    def __init__(self, ):
        self.di_all_cars = {}

    def register(self, name, num):
        if name not in self.di_all_cars:
            self.di_all_cars[name] = num
            return f'{name} registered {num} successfully'
        return f'ERROR: already registered with plate number {num}'

    def unregister(self, name):
        if name in self.di_all_cars:
            del self.di_all_cars[name]
            return f'{name} unregistered successfully'
        return f'ERROR: user {name} not found'

    def __str__(self):
        return '\n'.join(f'{k} => {v}' for k, v in self.di_all_cars.items())


parking = Parking()

for token in [input() for _ in range(int(input()))]:
    if 'unregister' in token:
        num, name = token.split()
        print(parking.unregister(name))
    else:
        command, name, num = token.split()
        print(parking.register(name, num))

print(parking)
