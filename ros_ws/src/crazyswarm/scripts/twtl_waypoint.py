#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *
from sensor_msgs.msg import Joy

class Waypoint:
    def __init__(self, agent, x, y, z, arrival, duration):
        self.agent = agent
        self.x = x
        self.y = y
        self.z = z
        self.arrival = arrival
        self.duration = duration

    def __lt__(self, other):
        return self.arrival < other.arrival

    def __repr__(self):
        return "Ag {} at {} s. [{}, {}, {}]".format(self.agent, self.arrival, self.x, self.y, self.z)


if __name__ == "__main__":

    # execute waypoints
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    # load csv file
    data = np.loadtxt("/home/ryan/Desktop/pyTWTL/output/waypoints_dynamic.csv", skiprows=1, delimiter=',')

    # sort by agents
    waypoints = []
    lastAgent = None

    if len(data.shape) == 1:
        waypoints.append(Waypoint(
	    int(data[0]), data[1], data[2], data[3], data[4], data[4]))
	lastAgent = int(data[0])
	print(waypoints)
    else:
        data[data[:,0].argsort()]
        # convert to internal data structure
        for row in data:
            waypoints.append(Waypoint(
	        int(row[0]),
	        row[1],
	        row[2],
	        row[3],
	        row[4],
	        row[4]))
            lastAgent = int(row[0])
        # sort waypoints by arrival time
        waypoints.sort()
        # print waypoints
        print(waypoints)

    for waypoint in waypoints:
        if waypoint.arrival == 0:
	    pos = [waypoint.x, waypoint.y, waypoint.z]
	    # print(waypoint.agent, pos, 2.0)
	    cf = allcfs.crazyfliesById[waypoint.agent]
	    cf.goTo(pos, 0, 1.5)
        elif waypoint.duration > 0:
	    pos = [waypoint.x, waypoint.y, waypoint.z]
	    cf = allcfs.crazyfliesById[waypoint.agent]
	    cf.goTo(pos, 0, waypoint.duration)

    # constant sleep interval for all
    timeHelper.sleep(waypoints[0].duration)

