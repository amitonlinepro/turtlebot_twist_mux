import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
import time

class TwistMux(Node):
    def __init__(self):
        super().__init__('twist_mux')

        qos_profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.RELIABLE)

        # Publishers & Subscribers
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription1 = self.create_subscription(Twist, '/teleop/cmd_vel', self.teleop_callback, qos_profile)
        self.subscription2 = self.create_subscription(Twist, '/random_mover/cmd_vel', self.random_mover_callback, qos_profile)

        self.current_twist = Twist()
        self.last_teleop_time = 0  # Time of the last teleop message
        self.teleop_active = False

        # Timer to check for teleop timeout (runs every 0.1 sec)
        self.timer = self.create_timer(0.1, self.check_timeout)

    def teleop_callback(self, msg):
        self.get_logger().info('Received teleop command')
        self.current_twist = msg
        self.publisher_.publish(self.current_twist)

        # Update teleop state
        self.last_teleop_time = time.time()
        self.teleop_active = True

    def random_mover_callback(self, msg):
        # Only publish if teleop is inactive
        if not self.teleop_active:
            self.get_logger().info('Using random mover')
            self.publisher_.publish(msg)

    def check_timeout(self):
        """Check if teleop has timed out, then switch back to random_mover."""
        if self.teleop_active and time.time() - self.last_teleop_time > 0.5:  # Timeout after 0.5 sec
            self.get_logger().info('Teleop timeout, switching back to random mover')
            self.teleop_active = False

def main(args=None):
    rclpy.init(args=args)
    node = TwistMux()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
