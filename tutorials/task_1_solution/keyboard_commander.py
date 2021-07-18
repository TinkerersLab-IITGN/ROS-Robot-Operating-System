#!/usr/bin/env python

# Create ROS node to publish on the ROS Topic "/turtle1/cmd_vel"
# to direct the turtle to travel in a circle

# Gives you access to python methods for creating
# ROS nodes and publisher and subscribers
import rospy

# Import the data type / message type for subscribing / publishing to ROS Topic
from geometry_msgs.msg import Twist

# For detecting key presses
import curses


def clear(ros_msg) :

    ros_msg.linear.x = 0
    ros_msg.linear.y = 0
    ros_msg.linear.z = 0

    ros_msg.angular.x = 0
    ros_msg.angular.y = 0
    ros_msg.angular.z = 0

    pass    

# My main code will perform this method continuously
def talker(win):

    # Code for key presses is copied from 
    # https://stackoverflow.com/a/32386410
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")

    # Declaring a publisher object to publish to /turtle1/cmd_vel
    # The message type for the topic /turtle1/cmd_vel is Twist
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist)

    # Creating a message template of Twist data class
    # for publishing to /turtle1/cmd_vel
    msg = Twist()
    
    # Initialize my ROS node
    rospy.init_node('souritra_the_pirate')
    
    # Main while loop
    while not rospy.is_shutdown():
        
        try :
            
            key = win.getkey()         
            win.clear()                
            win.addstr("Detected key:")
            win.addstr(str(key)) 
            
            clear(msg)

            if key == 'w' :

                msg.linear.x = 1
                pub.publish(msg)

            if key == 's' :

                msg.linear.x = -1
                pub.publish(msg)

            if key == 'a' :

                msg.angular.z = 1
                pub.publish(msg)

            if key == 'd' :

                msg.angular.z = -1
                pub.publish(msg)     

        except Exception as e :
            # If no key is pressed
            # win.getkey() throws an exception
            pass
    pass

try:
    
    curses.wrapper(talker)

except rospy.ROSInterruptException:
    
    pass