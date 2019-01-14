from setuptools import setup

setup(
    name="aws-snapshot-alyzer",
    version="0.1",
    author="Amarjeet Singh",
    author_email="a4amar97@gmail.com",
    description="This is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=["shotty"],
    url="https://github.com/AmarjeetSingh/aws-snapshot-alyzer",
    install_requires=[
        'click',
        'botocore',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:click
        ''',
)
