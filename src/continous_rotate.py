#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist

#from my_frontier_exploration_node import * 

def explore():
    # Initialize the node
    rospy.init_node('my_frontier_exploration_node', anonymous = True)
    rate = rospy.Rate(10)

    # Create a object for publishing on a topic
    velocity_pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)
    
    # Create a object for Twist Message
    twist_vel_msg = Twist()
    twist_stop_msg = Twist()

    # Speeds
    linear_speed = 5
    angular_speed = 1

    # Write the twist message using the object twist_vel_msg
    twist_vel_msg.linear.y = abs(linear_speed)
    twist_vel_msg.linear.y = 0
    twist_vel_msg.linear.z = 0
    twist_vel_msg.angular.x = 0
    twist_vel_msg.angular.y = 0
    twist_vel_msg.angular.z = abs(angular_speed)

    # Write the twist message using the object twist_stop_msg
    twist_stop_msg.linear.y = 0
    twist_stop_msg.linear.y = 0
    twist_stop_msg.linear.z = 0
    twist_stop_msg.angular.x = 0
    twist_stop_msg.angular.y = 0
    twist_stop_msg.angular.z = 0


    while not rospy.is_shutdown():
    
        # Publish the velocity
        velocity_pub.publish(twist_vel_msg)



    # Creating a class instance of frontier_exploration_node
    #turtlebot_explore = frontier_exploration_node()

    # Calling a class member function startExploration    
    #turtlebot_explore.startExploration()

    
    rospy.spin()

    return 




if __name__ == '__main__':
    try:
        explore()
    except rospy.ROSInterruptException:
        pass





