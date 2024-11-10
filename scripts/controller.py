#! /usr/bin/env python3
import time
import rospy
from tf.transformations import quaternion_from_euler
from mavros_msgs.msg import *
from mavros_msgs.srv import *
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import PoseStamped



class fcuModes(object):

    def __init__(self):
        self.tinggi = ??? #Set ketinggian sesuka

    def setTakeoff(self):

        rospy.wait_for_service('???')  #### Check for service
        try:
            takeoffService = rospy.ServiceProxy('???', ???)
            takeoffService(altitude = self.tinggi)
            rospy.loginfo(f"takeoff {self.tinggi} meter")  ### Call service and data type
            time.sleep(5)

        except rospy.ServiceException as e:
            rospy.logerr("Takeoff Failed")
    
    def setArm(self):
        rospy.wait_for_service('???')  #### Check for service
        try: 
            armService = rospy.ServiceProxy('???', ???)  ### Call service and data type
            armService(True)
            rospy.loginfo('arming')

        except rospy.ServiceException as e:
            rospy.logerr("Arming Failed")

    
    def setDisarm(self):
        rospy.wait_for_service('mavros/cmd/arming')
        try: 
            armService = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)
            armService(False)
            rospy.loginfo('disarming')

        except rospy.ServiceException as e:
            rospy.logerr("Arming Failed")

    def setGuided(self):
        rospy.wait_for_service('mavros/set_mode')
        try:
            guidedService = rospy.ServiceProxy('mavros/set_mode', SetMode)
            guidedService(custom_mode='GUIDED')
            rospy.loginfo('masuk mode guide')

        except rospy.ServiceException as e:
            rospy.logerr("Guided Failed")

    def setLand(self):
        rospy.wait_for_service('mavros/set_mode')
        try:
            landService = rospy.ServiceProxy('mavros/set_mode', SetMode)
            landService(custom_mode='LAND')
            rospy.loginfo("landing")
        except rospy.ServiceException as e:
            rospy.logerr("Land failed")

    
class controller:
    def __init__(self):
        
        rospy.Subscriber('mavros/state', State, self.state_cb)
        
        self.state = State()

        self.path = {}
        self.count_depan = 0
        self.county_bawah = 0

    def state_cb(self, msg):
        self.state = msg
    
    def posisi(self,x,y,z):
        pub_posisi = rospy.Publisher("/mavros/setpoint_position/local",PoseStamped,queue_size=10)
        posisi = PoseStamped()
        
        posisi.pose.position.x = x
        posisi.pose.position.y = y
        posisi.pose.position.z = z

        q = quaternion_from_euler(0.0,0.0,1.571)
        
        posisi.pose.orientation.x = q[0]
        posisi.pose.orientation.y = q[1]
        posisi.pose.orientation.z = q[2]
        posisi.pose.orientation.w = q[3] 

        pub_posisi.publish(posisi)

        rospy.loginfo(f"menuji point {x,y,z}")

        time.sleep(15)


def main():

    rospy.init_node('Controller', anonymous=True)
    rate = rospy.Rate(30.0)
    modes = #Class
    control = #Class
    
    modes.??? #Set MODE
    
    while not control.state.armed:
        modes.??? #Arm dulu bro
        rate.sleep()
    
    time.sleep(5)

    if control.state.armed:

        modes.setTakeoff()
        test = [[0,0,0],[0,0,2.5],[4,8.4,2],[-0.3,8.95,1.7],[-3.75,8.25,2.5],[-0.9,3.25,2.5]]
        for i in test:

            rate.sleep()
            control.posisi(i[0],i[1],i[2])
            rate.sleep()

        time.sleep(6)
        modes.??? #Panggil LAND


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


    
