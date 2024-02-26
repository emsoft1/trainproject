class MeasurementPoint:
    def __init__(self, location):
        self.location = location
        self.vibration = 0

    def calculate_vibration(self, train, faults=[]):
        distance = abs(train.position - self.location)
        self.vibration = train.weight * train.speed / max(distance, 1) ** 2
        # Simplified fault impact calculation
        for fault in faults:
            if (
                abs(fault["location"] - self.location) < 50
            ):  # Threshold for fault effect
                self.vibration *= fault["severity"]


class Track:
    def __init__(self, length, measurement_points_locations):
        self.length = length
        self.measurement_points = [
            MeasurementPoint(location) for location in measurement_points_locations
        ]
        self.faults = []

    def add_fault(self, fault_type, location, severity=1):
        self.faults.append(
            {"type": fault_type, "location": location, "severity": severity}
        )

    def calculate_vibrations(self, train):
        for point in self.measurement_points:
            point.calculate_vibration(train, self.faults)
