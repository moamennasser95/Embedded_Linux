from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    obj_launch=LaunchDescription()

    pub_node = Node(
        package = "iti_lab3",
        executable = "Pub_Node"
    )

    sub_node = Node(
        package = "iti_lab3",
        executable = "Sub_Node"
    )

    obj_launch.add_action(pub_node)
    obj_launch.add_action(sub_node)

    return obj_launch
