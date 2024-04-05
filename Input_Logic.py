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

    def enable_outputs(self):
        self.outputs_enabled = True

    def set_settings_1_flag(self):
        self.settings_flag = True

    def set_outputs(self):
        self.output_feedback_ok = True

    def check_output_feedback(self):
        return self.output_feedback_ok

    def save_switch_states(self):
        pass

    def set_display(self):
        pass

    def increment_output_state(self):
        self.output_feedback_ok = not self.output_feedback_ok

    def start_up_sequence(self):
        self.reset_fault_flag()
        if self.switch_states_changed:
            if self.more_than_one_active:
                self.set_settings_1_flag()
            else:
                self.set_outputs()
        else:
            if not self.override_detected:
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

    def run(self):
        self.override_detected = self.get_yes_no_input("Is an override command active? (yes/no): ")
        self.switch_states_changed = self.get_yes_no_input("Have switch settings changed? (yes/no): ")
        self.more_than_one_active = self.get_yes_no_input("Is more than one action active? (yes/no): ")
        self.output_feedback_ok = self.get_yes_no_input("Is the output feedback OK? (yes/no): ")

        result = self.start_up_sequence()
        print(result)
        if self.fault_flag:
            result = self.interrupt_sequence()
            print(result)

    @staticmethod
    def get_yes_no_input(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'no']:
                return response == 'yes'
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    simulator = BoatSensorSimulator()
    simulator.run()
