#!/bin/python3
import random
import traceback
import sys
import csv
from turn_decision_algorithm.math_functions import probable_turn

averages = {}
previous_values = {}
entry_lanes = []
exit_lanes = []

f = open('car_prob_values.csv', 'w')
w = csv.writer(f, dialect='excel-tab')
w.writerow(['car_id', 'vel', 'pos_x', 'pos_y',
            'pvel', 'ppos_x', 'ppos_y', 'prob'])


def add_entry_lane(lane_id):
    lane_id = lane_id.decode('utf-8')
    entry_lanes.append(lane_id)
    print("Entry lanes: " + str(entry_lanes))


def add_exit_lane(lane_id):
    lane_id = lane_id.decode('utf-8')
    exit_lanes.append(lane_id)
    print("Exit lanes: " + str(exit_lanes))


def detect_turn_car(velocity, pos_x, pos_y, car_id, lane_id):
    try:
        car_id = car_id.decode('utf-8')
        lane_id = lane_id.decode('utf-8')
        lane_id = lane_id[:-2]

        if lane_id in exit_lanes:
            return 0

        if car_id not in previous_values.keys():
            previous_values[car_id] = {
                'vel': velocity,
                'pos_x': pos_x,
                'pos_y': pos_y,
                'lane_id': lane_id
            }

            return 0

        pvel = previous_values[car_id]['vel']
        pposx = previous_values[car_id]['pos_x']
        pposy = previous_values[car_id]['pos_y']

        if car_id not in averages.keys():
            avg = 0
            averages[car_id] = {
                'sum': 0,
                'samples': 0
            }
        else:
            avg = float(averages[car_id]['sum']) / averages[car_id]['samples']

        result, value = probable_turn(
            pvel, (pposx, pposy), velocity, (pos_x, pos_y), prom=avg)

        averages[car_id]['sum'] += value
        averages[car_id]['samples'] += 1

        w.writerow([car_id, velocity, pos_x, pos_y,
                    pvel, pposx, pposy, value])

        return value

    except:
        traceback.print_exc(file=sys.stdout)
        return -1


if __name__ == '__main__':
    pass
