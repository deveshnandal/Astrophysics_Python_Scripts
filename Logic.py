# Python simulation of the boat sensor logic flow as per the provided flow diagram.

class BoatSensorSimulator:
    def __init__(self):
        self.fault_flag = False
        self.settings_flag = False
        self.override_detected = False
        self.switch_states_changed = False
        self.more_than_one_active = False
        self.output_feedback_ok = True
        self.outputs_enabled = False

    def reset_fault_flag(self):
        self.fault_flag = False

    def reset_settings_flag(self):
        self.settings_flag = False

    def check_override(self):
        return self.override_detected

    def enable_outputs(self):
        self.outputs_enabled = True

    def have_switch_settings_changed(self):
        return self.switch_states_changed

    def set_settings_1_flag(self):
        self.settings_flag = True

    def set_outputs(self):
        # For simulation purposes, we assume the outputs are set correctly.
        self.output_feedback_ok = True

    def check_output_feedback(self):
        return self.output_feedback_ok

    def save_switch_states(self):
        # Simulation of saving switch states to some storage.
        pass

    def set_display(self):
        # Simulation of setting display, which might involve some I/O operations.
        pass

    def increment_output_state(self):
        # For simulation purposes, we just toggle the feedback flag.
        self.output_feedback_ok = not self.output_feedback_ok

    def start_up_sequence(self):
        self.reset_fault_flag()
        if self.have_switch_settings_changed():
            if self.more_than_one_active:
                self.set_settings_1_flag()
            else:
                self.set_outputs()
        else:
            if not self.check_override():
                self.enable_outputs()

        if self.check_output_feedback():
            self.save_switch_states()
            self.set_display()
            return "System Started Successfully"
        else:
            return "Output Feedback Error"

    def interrupt_sequence(self):
        self.reset_settings_flag()
        self.set_settings_1_flag()
        self.fault_flag = True
        self.disable_outputs()
        if not self.check_output_feedback():
            self.increment_output_state()
            return "Interrupt Handled with Fault"
        else:
            return "Interrupt Handled Successfully"

    def disable_outputs(self):
        self.outputs_enabled = False

    # Run the startup sequence by default
    def run(self):
        result = self.start_up_sequence()
        print(result)
        # If a fault is detected, run the interrupt sequence
        if self.fault_flag:
            result = self.interrupt_sequence()
            print(result)

# Create an instance of the simulator
simulator = BoatSensorSimulator()

# We can manually set the conditions to test different paths
simulator.override_detected = False
simulator.switch_states_changed = True
simulator.more_than_one_active = True
simulator.output_feedback_ok = True

# Run the simulation
simulator.run()
