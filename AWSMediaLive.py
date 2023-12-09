#! python3

"""AWSMediaLive.py: Client for interacting with AWS MediaLive"""

import AWSConfig
import Utils


class AWSMediaLive(object):
    """
    Client for interacting with AWS MediaLive
    """

    def __init__(self, config: AWSConfig.AWSConfig):
        self.config = config
        self.client = self.config.session.client('medialive')
