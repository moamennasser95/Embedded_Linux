from setuptools import setup

package_name = 'ITI_LAB1'

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
    maintainer_email='moamen@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "str_publisher=ITI_LAB1.str_publisher:main" ,
        "number_counter=ITI_LAB1.number_counter:main"
        
        ],
    },
)
