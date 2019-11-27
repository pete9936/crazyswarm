#!/usr/bin/env python

import numpy as np
import rospy
import pdb
from tf import TransformListener
from geometry_msgs.msg import TransformStamped

from pycrazyswarm import *
import uav_trajectory


def callback(base_pose):
    print base_pose.transform.translation.x
    # x = base_pose.transform.translation.x
    # y = base_pose.transform.translation.y
    # z = base_pose.transform.translation.z
    # if (z < 0.15):
    #    z = 0.15
    # rate = rospy.Rate(10) # 10hz
    for cf in allcfs.crazyflies:
        pos = np.array([x, y+0.25, z+0.5])
        cf.hover(pos, 0, 1.0)

def base_listener():
    rospy.init_node('base_tf', anonymous=True) # this is a maybe
    rospy.Subscriber('/vicon/base/base', TransformStamped, callback)
    rospy.spin()


if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    Z = 1.0
    # allcfs.takeoff(targetHeight=Z, duration=1.4+Z)
    timeHelper.sleep(1.5+Z)
    # pdb.set_trace()
    try:
        base_listener()
    except KeyboardInterrupt:
        pass
    
    # allcfs.land(targetHeight=0.06, duration=1.0+Z)
    timeHelper.sleep(1.0)
