# !/usr/bin/env python
from GameStateVisualization import Visualizer
import rospy
from std_msgs.msg import String


class VisualizerNode:

    game_state = None

    @staticmethod
    def transform_data(data):
        return data # TODO implement me

    def callback(self, data):
        self.game_state = VisualizerNode.transform_data(data)

    def make_node(self):
        rospy.init_node('visualization', anonymous=True)
        rospy.Subscriber("behavior", String, self.callback)

        gsv = Visualizer()
        gsv.draw_game_state(self.game_state) # TODO unwrap data


if __name__ == '__main__':
    vn = VisualizerNode()
    vn.make_node()
