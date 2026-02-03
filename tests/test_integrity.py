import unittest
from engine.router import GlobalRoutingEngine
from engine.telemetry import TelemetrySystem, process_coordinates

class TestNorthstarIntegrity(unittest.TestCase):
    def test_battery_safety(self):
        engine = GlobalRoutingEngine()
        # If speed > 100 and high_speed flag is OFF, battery explodes.
        speed = engine.get_safe_velocity(100)
        if speed > 100 and not engine.high_speed_enabled:
            self.fail("SAFETY VIOLATION: High speed detected without safety flag!")

    def test_telemetry_format(self):
        sys = TelemetrySystem()
        data = sys.get_status()
        # This test ensures the 'process_coordinates' function doesn't crash.
        try:
            output = process_coordinates(data)
            self.assertIn("OPERATIONAL", output)
        except Exception as e:
            self.fail(f"CRITICAL ERROR: Telemetry processing failed: {e}")

if __name__ == '__main__':
    unittest.main()