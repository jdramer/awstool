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

    def describe_cf_distribution(self, cf_id):
        response = self.client.get_distribution(Id=cf_id)
        response = Utils.check_response(response)
        if response:
            dist = response['Distribution']
            Utils.dump_json(dist)
        return response
