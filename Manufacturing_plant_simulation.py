class Machine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.state = "off"
        self.total_count = 0
        self.good_count = 0
        self.reject_count = 0
        self.mode = "stopped"

    def turn_on(self):
        self.state = "on"

    def turn_off(self):
        self.state = "off"

    def set_mode(self, mode):
        self.mode = mode

    def produce(self):
        if self.state == "on" and self.mode == "producing":
            self.total_count += 1
            self.good_count += 1
        else:
            self.reject_count += 1

    def change_mode(self, mode):
        self.mode = mode

    def report_status(self):
        print(f"Machine ID: {self.machine_id}")
        print(f"State: {self.state}")
        print(f"Total Count: {self.total_count}")
        print(f"Good Count: {self.good_count}")
        print(f"Reject Count: {self.reject_count}")
        print(f"Mode: {self.mode}")


def test_simulation():
    # Create machines
    n = 5  # Number of machines
    machines = [Machine(i) for i in range(n)]

    # Turn on machines
    for machine in machines:
        machine.turn_on()

    # Set modes for machines
    modes = ["producing", "stopped", "changeover", "faulted"]
    for i, machine in enumerate(machines):
        machine.set_mode(modes[i % len(modes)])

    # Simulate production
    for machine in machines:
        machine.produce()

    # Change modes for machines
    for i, machine in enumerate(machines):
        machine.change_mode(modes[(i + 1) % len(modes)])

    # Report status of machines
    for machine in machines:
        machine.report_status()


# Run the simulation
test_simulation()