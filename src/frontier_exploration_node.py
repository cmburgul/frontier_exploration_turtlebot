#!/usr/bin/env python

import rospy
import time
from occupancy_map import * 

from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Header
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import numpy as np

class Frontier_Exploration():

    def __init__(self):

        self.rate = rospy.Rate(15)

        # Create a variable for publishing on a topic /mobile_base/commands/velocity
        self.velocity_pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)
          
        # Create a variable for Twist Message
        self.twist_msg = Twist()

        # Create a variable for publishing on a topic /visualization_marker
        self.marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size = 10) 

        # Speed varaibles
        self.linear_speed = 5
        self.angular_speed = 1       

    def rotate(self):
        rospy.loginfo("Rotating...")
        # Write the twist message to twist_vel_msg variable
        self.twist_msg.linear.y = 0
        self.twist_msg.linear.y = 0
        self.twist_msg.linear.z = 0
        self.twist_msg.angular.x = 0
        self.twist_msg.angular.y = 0
        self.twist_msg.angular.z = 5   

        # Publish the velocity
        self.velocity_pub.publish(self.twist_msg)

        time.sleep(10) # Sleeps for ten seconds

        # Set angular velocity as zero
        self.twist_msg.angular.z = 0

        # Stop Rotation
        self.velocity_pub.publish(self.twist_msg)        

    def mapCallback(self, msg):
        #print(msg)
        width  = msg.info.width
        height = msg.info.height

        print ("width ", width)
        print ("height ", height)

        # Creating a variable for Occupancygrid
        grid_data = OccupancyGrid()
        # Pushing the topic Occupancygrid.data to grid_data
        grid_data = msg.data # Flattened tuple

        # Converting the grid_data(flattened tuple) to a numpy array
        map_array = []
        map_array = np.array(grid_data)

        print(map_array)
        print ("shape", map_array.shape)

        # Reshaping the flattened array to array of array
        map_array = np.reshape(map_array, (width, height))

        print (map_array.shape)

        # Count number of grids with types
        print_grid_types(map_array)

        # Seperatinf frontier points from the occupancy map
        frontiers = []
        frontiers = get_frontiers(width, height, map_array)

        # Find Centroid of frontiers
        centroid = []
        centroid = get_frontier_centroid(frontiers)
        
        print ("Centroid : ",centroid)

        # Visualize the centroid point on Rviz using markers
        visualize_centroid(centroid, self.marker_pub)
        
        # Give the centroid to the move_base action client


    def startExploration(self):
        rospy.loginfo("Starting the robot")

        """
        rospy.loginfo("Robot set to rotate for 10 seconds")
        self.rotate()
        rospy.loginfo("Robot stopped rotating")
        """


        # Create a variable for subscribing on a topic /map
        #self.map_ = rospy.Subscriber("/map", OccupancyGrid, mapCallback)
        rospy.Subscriber("/map", OccupancyGrid, self.mapCallback)  

        rospy.loginfo("Read /OccupancyGrid topic")
        



        
        #print(self.map_)

        rospy.sleep(10)

        # Get frontier points and its count










            






        



    