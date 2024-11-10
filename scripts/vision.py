#!/usr/bin/env python3
from __future__ import print_function
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub2 = rospy.Subscriber("???", ???, self.callback)  ### Panggil topik dan data type

  def callback(self, data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
    except CvBridgeError as e:
      print(e)
    
    cv2.imshow("Kamera Depan", ???)  ### Ape ni
    cv2.waitKey(3)

def main(args):
  ic = #class
  rospy.init_node('image_front', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main(sys.argv)
