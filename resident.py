"""
Residential Class
Created by: Shijin (Kevin) Yang
"""

import get_buildings

class Residence:
    def __init__(self, name, num, attrs):
        self.name = name
        self.num = num
        self.attributes = attrs
    def num_of_students(self):
        return self.num
    def get_name(self):
        return self.name

residents = ["V1", "REV", "UWP", "MKV", "STP", "SJ"]
b_lst = get_buildings.uw.building_list()
output = get_buildings.filter_buildings(residents, b_lst)
print(len(output))
print(output)

instance_lst = []
for i,resi in enumerate(residents):
    ins = Residence(resi, 0, b_lst[i])
    instance_lst.append(ins)
    
print(instance_lst)
print(instance_lst[0].get_name())