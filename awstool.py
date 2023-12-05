#! python3

"""awstool.py: Tool for automating AWS pipeline creation"""
import argparse

import AWSConfig
import AWSMediaPackage


if __name__ == "__main__":

    # Set up config
    config = AWSConfig.AWSConfig()
    config.init_from_ini("aws.ini", "us-west-2")


