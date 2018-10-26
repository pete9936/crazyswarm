def callback(base_pose):
    x = base_pose.transform.translation.x
    y = base_pose.transform.translation.y
    z = base_pose.transform.translation.z
    if (z < 0.15):
        z = 0.15

    for cf in allcfs.crazyflies:
        pos = np.array([x, y+0.25, z+0.5])
        cf.hover(pos, 0, 1.0)

def base_listener():
    rospy.Subscriber('/vicon/base/base', TransformStamped, callback)
    rospy.spin()


if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    Z = 1.0
    allcfs.takeoff(targetHeight=Z, duration=1.0+Z)
    timeHelper.sleep(1.5+Z)

    try:
        base_listener()
    except KeyboardInterrupt:
        pass
    
    allcfs.land(targetHeight=0.06, duration=1.0+Z)
    timeHelper.sleep(1.0)
