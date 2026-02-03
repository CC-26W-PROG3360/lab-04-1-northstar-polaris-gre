class TelemetrySystem:
    def get_status(self):
        # CURRENT STATE: Returns a LIST [Status, Latitude, Longitude]
        # TEAM ALPHA (Git Flow): You will change this to a DICTIONARY in your branch.
        return ["OPERATIONAL", 45.523, -122.676]

def process_coordinates(data):
    status = data[0]
    lat = data[1]
    return f"Drone is {status} at Lat: {lat}"