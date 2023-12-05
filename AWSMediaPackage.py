#! python3

"""AWSMediaPackage.py: Client for interacting with AWS MediaPackage"""

import AWSConfig
import Utils


class AWSMediaPackage(object):
    """
    Client for interacting with AWS MediaPackage
    """

    def __init__(self, config: AWSConfig.AWSConfig):
        self.config = config
        self.client = self.config.session.client('mediapackage')

    def describe_mp_channel(self, mp_channel_id):
        pass
