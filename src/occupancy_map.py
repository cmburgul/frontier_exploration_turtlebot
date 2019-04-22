from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
import numpy as np
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import rospy


def is_valid(i, j, w, h):
    flag= False
    if (i > 0 and i < w and j > 0 and j < h):
        flag = True
    else:
        flag = False
    return flag

def print_grid_types(map_array):

    # Iterating through the arrays
    # Map values {-1 : Unknown, 0 : Completely free, 100 : Occupied } 
    # Count variables for all types of points
    unknown = 0
    free_space = 0
    occupied = 0

    # A array to store free_space_points
    free_space_points = []

    # Get the number of unknown grids, free_space grids and occupied grids
    for x in xrange(map_array.shape[0]):
        for y in xrange(map_array.shape[1]):
            #print ( "(%i, %i) : %i" %(x, y, map_array[x, y]) )
            if (map_array[x, y] == -1):
                unknown = unknown + 1
            elif (map_array[x, y] == 0):
                free_space = free_space + 1
                free_space_points.append((x,y))
            elif (map_array[x, y] > 0):
                occupied = occupied + 1

    print ("Total unknown cells :", unknown)
    print ("Total free cells :", free_space)
    print ("Total occupied cells :", occupied)

    print (len(free_space_points))
    #print (free_space_points)

def get_frontiers(width, height, map_array):
    # Seperating Frontiers from a free_space_points 
    
    # A array to store free_space_points
    free_space_points = []
    # Get the free_space grids
    for x in xrange(map_array.shape[0]):
        for y in xrange(map_array.shape[1]):
            #print ( "(%i, %i) : %i" %(x, y, map_array[x, y]) )
            if (map_array[x, y] == 0):
                free_space_points.append((x,y))

    count = 0
    frontier = []
    for x in free_space_points:
        # print (x[0], x[1]) 
        i = x[0]
        j = x[1]
        

        flag = False
        # front node (i+1, j)
        flag_front = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False 
        # Checking 4 point in front of (i, j) for an unknown point
        if (is_valid(i+1, j, width, height)):
            if ( (map_array[i+1][j] == -1) ):
                flag1 = True
        if (is_valid(i+2, j, width, height)):
            if ( (map_array[i+2][j] == -1) ):
                flag2 = True
        if (is_valid(i+3, j, width, height)):
            if ( (map_array[i+3][j] == -1) ):
                flag3 = True
        if (is_valid(i+4, j, width, height)):
            if ( (map_array[i+4][j] == -1) ):
                flag4 = True
        if ( (flag1 == True)  and (flag2 == True) ):# and (flag3 == True) and (flag4 == True) ):
            flag_front = True
            count  = count + 1

        # top node (i, j+1)
        flag_top = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False 

        if (is_valid(i, j+1, width, height)):
            if ( (map_array[i][j+1] == -1) ):
                flag1 = True
        if (is_valid(i, j+2, width, height)):
            if ( (map_array[i][j+2] == -1) ):
                flag2 = True
        if (is_valid(i, j+3, width, height)):
            if ( (map_array[i][j+3] == -1) ):
                flag3 = True
        if (is_valid(i, j+4, width, height)):
            if ( (map_array[i][j+4] == -1) ):
                flag4 = True
        if ( (flag1 == True)  and (flag2 == True) ):# and (flag3 == True) and (flag4 == True) ):
            flag_top = True
            count  = count + 1

        # left node (i-1, j)
        flag_left = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False 

        if (is_valid(i-1, j, width, height)):
            if ( (map_array[i-1][j] == -1) ):
                flag1 = True
        if (is_valid(i-2, j, width, height)):
            if ( (map_array[i-2][j] == -1) ):
                flag2 = True
        if (is_valid(i-3, j, width, height)):
            if ( (map_array[i-3][j] == -1) ):
                flag3 = True
        if (is_valid(i-4, j, width, height)):
            if ( (map_array[i-4][j] == -1) ):
                flag4 = True
        if ( (flag1 == True) and (flag2 == True)  ):# and (flag3 == True) and (flag4 == True) ):
            flag_left = True
            count  = count + 1

        # down node (i, j-1)
        flag_down = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False 

        if (is_valid(i, j-1, width, height)):
            if ( (map_array[i][j-1] == -1) ):
                flag1 = True
        if (is_valid(i, j-2, width, height)):
            if ( (map_array[i][j-2] == -1) ):
                flag2 = True
        if (is_valid(i, j-3, width, height)):
            if ( (map_array[i][j-3] == -1) ):
                flag3 = True
        if (is_valid(i, j-4, width, height)):
            if ( (map_array[i][j-4] == -1) ):
                flag4 = True
        if ( (flag1 == True) and (flag2 == True) ):# and (flag3 == True) and (flag4 == True) ):
            flag_down = True
            count  = count + 1

        if ( (flag_front == True) or (flag_top == True) or (flag_left == True) or (flag_down == True) ):
            flag = True

        if (flag == True):
            frontier.append((i, j))
        
    print ("Count : ", count)
    #print ("frontier : ", frontier)
    print ("Number of Frontiers ", len(frontier))
    #print (frontier)

    return frontier

def get_frontier_centroid(frontiers):
    sumX = 0
    sumY = 0
    centroid = []

    for point in frontiers:
        sumX = sumX + point[0]
        sumY = sumY + point[1]
    centroid = [(sumX/len(frontiers)), (sumY/len(frontiers)) ]

    return centroid

def visualize_centroid(centroid, marker_pub):

    # Create a variable fr Marker Message
    marker = Marker()
    point = Point()

    # Fill the point message
    point.x = centroid[0]
    point.y = centroid[1]
    point.z = 0

    marker.header.frame_id = "/map"
    marker.header.stamp = rospy.get_rostime
    marker.type = marker.POINTS
    marker.action = marker.ADD
    marker.pose.orientation.w = 1
    marker.points = point
    t = rospy.Duration()
    marker.lifetime = t
    marker.scale.x = 0.4
    marker.scale.y = 0.4
    marker.scale.z = 0.4
    marker.color.a = 1.0
    marker.color.r = 1.0

    marker_pub.publish(marker)



    