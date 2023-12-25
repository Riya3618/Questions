#Q6

class GravitySimulation:
   def turn(self):
        self._map = [list(x)[::-1] for x in zip(*self._map)]
   def process_and_count_load_after_tilting(self, initial_map):
        self._map = [list(line) for line in initial_map]
        self.tilt()
        return self.calculate_total_load()
   def calculate_total_load(self):
        height = len(self._map)
        return sum((height - i) * sum(1 for char in line if char == "O") for i, line in enumerate(self._map))

   def simulate_gravity_over_time(self, initial_map):
        self._map = [list(line) for line in initial_map]

        total_cycles = 1000000000
        cache = {}

        for cycle_idx in range(total_cycles):
            for _ in range(4):
                self.tilt()
                self.turn()

            current_state_hash = hash("".join("".join(x) for x in self._map))

            if current_state_hash not in cache:
                cache[current_state_hash] = cycle_idx
            else:
                cycle_difference = cycle_idx - cache[current_state_hash]
                initial_cycle = cache[current_state_hash]
                remaining_cycles = total_cycles - ((total_cycles - initial_cycle) // cycle_difference) * cycle_difference - initial_cycle - 1
                break

        for _ in range(remaining_cycles):
            for _ in range(4):
                self.tilt()
                self.turn()

        return self.calculate_total_load()

   def tilt(self):
        columns = zip(*self._map)
        tilted_columns = []

        for column in columns:
            parts = "".join(column).split("#")
            tilted_parts = [("O" * segment.count("O")).ljust(len(segment), ".") for segment in parts]
            tilted_columns.append("#".join(tilted_parts))

        self._map = [list(x) for x in zip(*tilted_columns)]
