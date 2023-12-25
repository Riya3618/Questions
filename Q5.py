#Q5
from functools import reduce

class Solution:
    def custom_function_1(self, data):
        processed_data = data[0].split(",")
        return sum(self.calculate_hash(item) for item in processed_data)

    def custom_function_2(self, data):
        processed_data = data[0].split(",")
        custom_groups = [{} for _ in range(256)]

        for line in processed_data:
            if "=" in line:
                label, value = line.split("=")
                group_id = self.calculate_hash(label)
                custom_groups[group_id][label] = int(value)
            else:
                label = line[:-1]
                group_id = self.calculate_hash(label)
                if label in custom_groups[group_id]:
                    del custom_groups[group_id][label]

        power = 0
        for group_id, grp in enumerate(custom_groups, 1):
            for slot_id, lens in enumerate(grp.items(), 1):
                power += group_id * slot_id * lens[1]

        return power

    def calculate_hash(self, item):
        return reduce(lambda acc, c: (acc + ord(c)) * 17 % 256, item, 0)
