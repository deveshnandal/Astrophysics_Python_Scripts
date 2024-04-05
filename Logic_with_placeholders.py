import time

# Extending the BoatSensorSimulator class to include output states and flag indications
class BoatSensorSimulator:
    def __init__(self):
        self.fault_flag = False
        self.settings_flag = False
        self.override_detected = False
        self.switch_states_changed = False
        self.more_than_one_active = False
        self.output_feedback_ok = True
        self.outputs_enabled = False
        self.nav_switch_position = 0
        self.anchor_switch = False
        # Outputs are represented as a dictionary with their state (True for ON, False for OFF)
        self.outputs = {
            'LNP': False,  # Lower Navigation Port
            'LNS': False,  # Lower Navigation Starboard
            'LNR': False,  # Lower Navigation Stern
            'STM': False,  # Steam light
            'TRI': False,  # Tricolour light
            'MST': False   # Masthead light
        }

    def update_outputs(self):
        # Reset all outputs
        for key in self.outputs:
            self.outputs[key] = False
        # Set outputs based on NAV switch position and anchor switch
        if self.nav_switch_position == 1:
            self.outputs.update({'TRI': True, 'MST': True})
        elif self.nav_switch_position == 2:
            self.outputs.update({'LNP': True, 'LNS': True, 'LNR': True, 'STM': True, 'MST': True})
        if self.anchor_switch:
            self.outputs['MST'] = True

    def display_outputs(self):
        for output, state in self.outputs.items():
            print(f"{output}: {'ON' if state else 'OFF'}")

    def display_flag(self, flag, symbol):
        print(f"{flag} Flag: {symbol}")

    def simulate_display(self):
        # This would be where the display logic would go, updating the display based on the output states.
        print("Displaying lights:")
        self.display_outputs()
        # Simulate Fault Flag
        fault_symbol = '!' if self.fault_flag else ' '
        self.display_flag("Fault", fault_symbol)
        # Simulate Settings Flag
        settings_symbol = '⚙️' if self.settings_flag else ' '
        self.display_flag("Settings", settings_symbol)

    def run(self):
        self.nav_switch_position = int(input("Enter NAV switch position (0, 1, 2): "))
        self.anchor_switch = input("Is the anchor switch active? (yes/no): ").lower() == 'yes'
        self.update_outputs()
        self.simulate_display()

        # Placeholder for the rest of the simulation logic
        # ...

if __name__ == "__main__":
    simulator = BoatSensorSimulator()
    simulator.run()
