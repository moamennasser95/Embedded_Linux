from setuptools import setup

package_name = 'iti_lab7'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='moamen',
    maintainer_email='moamennasser95@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        
        "node_task1=iti_lab7.node_task1:main" ,	#Pub_Node(any name)       .node1(nodename which is .py but without .py )
        "node_task1=iti_lab7.node_task2:main" ,	#Sub_Node(any name)	   .node2(nodename which is .py but without .py )
        ],
    },
)
