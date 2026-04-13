import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class FaceTracker(Node):
    def __init__(self):
        super().__init__('face_tracker_node')
        
        # LAG FIX: Change queue size from 10 to 1. We only want real-time data!
        self.subscription = self.create_subscription(
            Image,
            '/image_raw', 
            self.image_callback,
            1) 
            
        self.publisher_ = self.create_publisher(Image, '/face_tracking/output', 1)
        
        self.br = CvBridge()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # DETECTION FIX: Create a CLAHE object for smart contrast adjustment
        self.clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        
        self.get_logger().info('Face Tracker Node is active. Waiting for camera feed...')

    def image_callback(self, data):
        try:
            cv_image = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

            # Apply the smart CLAHE contrast fix
            gray = self.clahe.apply(gray)

            # Tweak the detection parameters to be a bit more forgiving
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(40, 40))

            for (x, y, w, h) in faces:
                cv2.rectangle(cv_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            output_msg = self.br.cv2_to_imgmsg(cv_image, encoding="bgr8")
            self.publisher_.publish(output_msg)
            
        except Exception as e:
            self.get_logger().error(f'Error processing image: {e}')

def main(args=None):
    rclpy.init(args=args)
    face_tracker = FaceTracker()
    
    try:
        rclpy.spin(face_tracker)
    except KeyboardInterrupt:
        pass
    finally:
        face_tracker.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
