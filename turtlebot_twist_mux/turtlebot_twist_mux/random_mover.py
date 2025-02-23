import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RandomMover(Node):
    def __init__(self):
        super().__init__('random_mover')
        self.publisher_ = self.create_publisher(Twist, '/random_mover/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_randomly)

    def move_randomly(self):
        msg = Twist()
        msg.linear.x = random.uniform(-0.5, 0.5)
        msg.angular.z = random.uniform(-1.0, 1.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: linear={msg.linear.x}, angular={msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
