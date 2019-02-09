"""
Pull data from uwaterlooapi - residence
Created by: Shijin (Kevin) Yang
"""

from uwaterlooapi import UWaterlooAPI

# connect with api_ley
uw = UWaterlooAPI(api_key="c6fe03239babd8c06f887524fa0aeb12")

def filter_buildings(buildings, whole_buildings):
    out = []
    for required_building in buildings:
        for item in whole_buildings:
            if item['building_code'] == required_building:
                out.append(item)
    return out