#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist

from frontier_exploration_node import * 

def explore():
    # Initialize the node
    rospy.init_node('my_frontier_exploration_node', anonymous = True)

    # Creating a class instance of frontier_exploration_node
    turtlebot_explore = Frontier_Exploration()

    # Calling a class member function startExploration    
    turtlebot_explore.startExploration()

    rospy.spin()

    return 

if __name__ == '__main__':
    try:
        explore()

    except rospy.ROSInterruptException:
        pass





