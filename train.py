class Train:
    def __init__(self, weight, speed):
        self.weight = weight
        self.speed = speed
        self.position = 0

    def update_position(self, time_interval):
        self.position += self.speed * time_interval
        self.position %= 1000  # Loop around for simplicity
