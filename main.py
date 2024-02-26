from train import Train
from track import Track
import visualization
import time

train = Train(weight=10000, speed=30)
track = Track(length=1000, measurement_points_locations=[200, 500, 800])
screen = visualization.initialize_screen(800, 600)

running = True
while running:
    train.update_position(0.05)
    track.calculate_vibrations(train)
    visualization.draw_simulation(screen, track, train)
    time.sleep(0.05)
    # Event handling and loop control logic here

visualization.close()
