import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from px4_msgs.msg import MotorCommands

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(MotorCommands, '/fmu/in/motor_commands', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = MotorCommands()
        msg.timestamp = self.get_clock().now().nanoseconds // 1000  # microseconds
        msg.commands = [0.5, 0.5, 0.5, 0.5]  # 4个电机的标准化命令 (0.0-1.0)
        msg.source = 1 # 命令来源 (0:未知, 1:ROS, 2:遥控器)
        # msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.commands)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()