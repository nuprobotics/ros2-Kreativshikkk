from setuptools import find_packages, setup

package_name = 'task01'

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

    maintainer='maintainer.name',

    maintainer_email='maintainer@email.com ',

    license='TODO',

    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # имя_исполняемого = пакет.модуль:функция_main
            'node = task01.node:main',
        ],
    },
)
