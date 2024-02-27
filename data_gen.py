from train import Train
from track import Track
import numpy as np
import pandas as pd
import time

full_time = 60  # each t i 0.5 sec that means 30 sec for the value of the 60
data = []
for loop in range (0 , 100 ):

    track = Track(length=1000, measurement_points_locations=[200, 500, 800])
    train = Train(weight=np.random.randint(2000 ,high= 10000), speed=np.random.randint(30 ,high= 50))
    track.add_fault('crack', np.random.randint(100 ,high= 900), severity=np.random.randint(1 ,high= 5))
    i = 0
    print (track.faults[0].fault_type)

    obj = {}
    while i <= 60:
        train.update_position(0.5)
        track.calculate_vibrations(train)
        obj[f"{i}_200"] = track.measurement_points[0].vibration
        obj[f"{i}_500"] = track.measurement_points[1].vibration
        obj[f"{i}_800"] = track.measurement_points[2].vibration
        # Event handling and loop control logic here

        i += 1

    obj["train_weight"] = train.weight
    obj["train_speed"] = train.speed
    obj["fault_type"] = track.faults[0].fault_type
    obj["fault_dis"] = track.faults[0].location
    obj["fault_severity"] = track.faults[0].severity


    data.append(obj)
    print (loop)
df = pd.DataFrame(data=data)
df.to_csv("newf1.csv")
print(data)
