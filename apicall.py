from uwaterlooapi import UWaterlooAPI

uw = UWaterlooAPI(api_key="c6fe03239babd8c06f887524fa0aeb12")

buildings = uw.building_list()

print(buildings[0])