from train import Train
from track import Track
import numpy as np
import pandas as pd
import time

full_time = 60  # each t i 0.5 sec that means 30 sec for the value of the 60
data = []
for loop in range (0 , 10 ):

    track = Track(length=1000, measurement_points_locations=[200, 500, 800])
    train = Train(weight=np.random.randint(2000 ,high= 10000), speed=np.random.randint(30 ,high= 50))

    i = 0

    obj = {}
    while i <= 60:
        train.update_position(0.5)
        track.calculate_vibrations(train)
        obj[f"{i}_200"] = track.measurement_points[0].vibration
        obj[f"{i}_500"] = track.measurement_points[1].vibration
        obj[f"{i}_800"] = track.measurement_points[2].vibration
        # Event handling and loop control logic here
        time.sleep(0.001)
        i += 1

    obj["train_weight"] = train.weight
    obj["train_speed"] = train.speed
    data.append(obj)
df = pd.DataFrame(data=data)
df.to_csv("new.csv")
print(data)
