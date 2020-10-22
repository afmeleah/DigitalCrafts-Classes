class Vehicle:
    def __init__(self, top_speed, acceleration):
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.speed = 0
        self.position = 0

    def move(self):
        self.accelerate()
        self.position += self.speed
    
    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed
    
    def reset(self):
        self.position = 0
        self.speed = 0

all_cars = {
"bike" : Vehicle(150, 10),
"car" : Vehicle(100, 20),
"truck" : Vehicle(200, 5),
}

def run_race(time):
    for car_name in all_cars:
        all_cars[car_name].reset()

    for i in range(time):
        for car_name in all_cars:
                all_cars[car_name].move()

    for car_name in all_cars:
        print(f"{car_name} - {all_cars[car_name].position}")

run_race(20)

run_race(40)

run_race(60)
