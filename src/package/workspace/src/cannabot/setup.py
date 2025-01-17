from setuptools import find_packages, setup

package_name = 'cannabot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rizzi26',
    maintainer_email='marco.meneguetti@sou.inteli.edu.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		    "cannabot = cannabot.cannabot:main",
            "lidar = cannabot.lidar:main",
            "lidar_teste = cannabot.lidar_teste:main",
            'teste_temp = cannabot.teste_temp:main',
            "odometry = cannabot.odometry:main",
        ],
    },
)
