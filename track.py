class MeasurementPoint:
    def __init__(self, location):
        self.location = location
        self.vibration = 0

    def base_vibration(self, train):
        # Example calculation for base vibration
        distance = abs(self.location - train.position)
        if distance == 0:
            return train.weight * train.speed  # Maximum vibration when train is at the measurement point
        return (train.weight * train.speed) / (distance ** 2)  # Decreases with distance

    def calculate_vibration(self, train, faults):
        base_vibration = self.base_vibration(train)
        total_fault_impact = 0

        for fault in faults:
            distance_to_fault = abs(self.location - fault.location)
            distance_to_train = abs(self.location - train.position)
            fault_impact = fault.impact(distance_to_fault)

            # Adjust fault impact based on train's position relative to the fault
            if train.position < fault.location:  # Train is before the fault
                fault_impact *= 0.5  # Example adjustment
            elif train.position > fault.location:  # Train is after the fault
                fault_impact *= 1.5  # Example adjustment

            total_fault_impact += fault_impact

        self.vibration = base_vibration + total_fault_impact


class Fault:
    def __init__(self, fault_type, location, severity):
        self.fault_type = fault_type
        self.location = location
        self.severity = severity

    def impact(self, distance):
        # Define how each fault type impacts vibration based on distance from the fault
        if self.fault_type == 'loose bolt':
            return self.severity / (distance + 1)  # Example impact function
        elif self.fault_type == 'crack':
            return self.severity * (1 / (distance + 1))  # Another impact function
        elif self.fault_type == 'weight':
            # Weight might have a constant effect regardless of distance, up to a certain point
            return self.severity if distance < 50 else 0  # Example logic

class Track:
    def __init__(self, length, measurement_points_locations):
        self.length = length
        self.measurement_points = [MeasurementPoint(location) for location in measurement_points_locations]
        self.faults = []

    def add_fault(self, fault_type, location, severity=1):
        self.faults.append(Fault(fault_type, location, severity))

    def calculate_vibrations(self, train):
        for point in self.measurement_points:
            point.calculate_vibration(train, self.faults)
