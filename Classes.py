class Vehicle:
    is_engine_on = False
    is_headlight_on = False
    is_driving = False
    make = None
    model = None

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'{self.make} {self.model} with engine '
                f'{"on" if self.is_engine_on else "off"} and headlight '
                f'{"on" if self.is_headlight_on else "off"}')


    def turn_engine_on(self):
        print('Turning engine on')
        self.is_engine_on = True

    def turn_engine_off(self):
        print('Turning engine off')
        if self.is_driving:
            print('Your tried to turn engine off while driving, and crashed')
            return
    
        self.is_engine_on = False

    def turn_headlight_on(self):
        print('Turning headlight on')
        self.is_headlight_on = True
    
    def turn_headlight_off(self):
        print('Turning headlight off')
        self.is_headlight_on = False

    def start_driving(self):
        if not self.is_engine_on:
            print("You can't drive without turning the engine on")
            return
        print('Start Driving')
        self.is_driving = True

    def stop_driving(self):
        print('Stop Driving')
        self.is_driving = False


class Motorcycle(Vehicle):
    def lean(self,direction):
        if not self.is_driving:
            print('you leaned while not driving, and crashed')
            return
        print(f'Leaning {direction}')
    

    def turn_handelbars(self, direction):
        print(f'Turning handelbars {direction}')


    def turn(self, direction):
        if direction == 'Left':
            self.turn_hendelbars('Right')
            self.lean('Left')
        elif direction == 'Right':
            self.turn_hendelbars('Left')
            self.lean('Right')
        else:
            print("Didn't understand that direction")
    

class Car(Vehicle):
    def turn_steering_wheel(self, direction):
        print(f'Turning steering wheel {direction}')


    def turn(self, direction):
        if direction in ['Left','Right']:
            self.turn_steering_wheel(direction)
        else:
            print("Didn't understand that direction")


# moto = Motorcycle('Triumph', 'Thruxton')
# car = Car('Honda','Civic')

# for vehicle in [moto, car]:
#     print(vehicle)
#     vehicle.turn_engine_on()
#     vehicle.turn_headlight_on()
#     vehicle.start_driving()
#     vehicle.turn('left')
#     vehicle.turn('right')
#     vehicle.stop_driving()
#     vehicle.turn_engine_off()
#     vehicle.turn_headlight_off()
#     print()



