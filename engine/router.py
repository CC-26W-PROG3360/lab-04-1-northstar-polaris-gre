import os


class GlobalRoutingEngine:
    def __init__(self):
        # Feature Flag: High Speed Mode (Defaults to False for safety)
        self.high_speed_enabled = (
            os.getenv("FEATURE_HIGH_SPEED", "false").lower() == "true"
        )

    def get_safe_velocity(self, current_altitude):
        """Calculates speed. If High Speed is off, we cap at 50 units."""
        if self.high_speed_enabled:
            # Your task is to change this to 150,
            # but ONLY if the flag is active.
            return 50

        # Standard safety speed
        return 50

    def calculate_path(self, start, end):
        # Logic for A* pathfinding (Simulation)
        return f"Routing from {start} to {end} at {self.get_safe_velocity(100)} knots."

    def calcuate_drone_height():
        # TODO: Add the drone code in the future
        return 1
