#! python3

"""AWSCloudFront.py: Client for interacting with AWS CloudFront"""

import AWSConfig
import Utils


class AWSCloudFront(object):
    """
    Client for interacting with AWS CloudFront
    """

    def __init__(self, config: AWSConfig.AWSConfig):
        self.config = config
        self.client = self.config.session.client('cloudfront')
