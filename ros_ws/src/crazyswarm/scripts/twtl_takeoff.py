#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    allcfs.takeoff(targetHeight=0.4, duration=1.5)
    timeHelper.sleep(2.0)
