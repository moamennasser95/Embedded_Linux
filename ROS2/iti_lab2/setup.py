from setuptools import setup

package_name = 'iti_lab2'

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
        "Int_publisher=iti_lab2.Int_publisher:main" ,
        #"number_counter=ITI_LAB1.number_counter:main"
        ],
    },
)
