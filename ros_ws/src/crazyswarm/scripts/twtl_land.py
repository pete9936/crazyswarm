#!/usr/bin/env python

import numpy as np
import pdb
from pycrazyswarm import *


if __name__ == "__main__":

    # load csv file
    data = np.loadtxt("/home/ryan/Desktop/pyTWTL/output/agents_land.csv").reshape((-1))

    # convert to internal data structure
    agents = []
    for agent in data:
        agents.append(int(agent))

    # execute land command
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    for agent in agents:
        cf = allcfs.crazyfliesById[agent]
	cf.land(targetHeight=0.04, duration=2.0)
    
    timeHelper.sleep(1.0) # maybe delete
