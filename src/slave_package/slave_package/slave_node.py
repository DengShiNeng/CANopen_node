import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from send_can_msgs.msg import SendMotorCommands
from recive_can_msgs.msg import ReciveMotorCommands


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('master_node')
        self.publisher_ = self.create_publisher(ReciveMotorCommands, '/can/out/motor_commands', 10)
        self.subscrip_ = self.create_subscription(SendMotorCommands, '/can/in/motor_commands', self.subscrip_callback, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = ReciveMotorCommands()
        msg.node = 2
        msg.str = "Hello"
        msg.vaule = 200
        self.publisher_.publish(msg)
        

    def subscrip_callback(self, msg):
        self.get_logger().info('Subscrip: "%d, %s, %d"' % (msg.node, msg.str, msg.vaule))



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()