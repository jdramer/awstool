#! python3

"""AWSCloudFront.py: Client for interacting with AWS CloudFront"""

import AWSConfig
import Utils
import urllib.parse
import uuid


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

    def create_cf_distribution(self, mpoe_url, id_segment):
        mp_host = urllib.parse.urlparse(mpoe_url).hostname
        response = self.client.create_distribution(DistributionConfig={
            "CallerReference": uuid.uuid4().__str__(),
            "Origins": {
                "Quantity": 1,
                "Items": [
                    {
                        "Id": mp_host,
                        "DomainName": mp_host,
                        "CustomOriginConfig": {
                            "HTTPPort": 80,
                            "HTTPSPort": 443,
                            "OriginProtocolPolicy": "https-only"
                        }
                    }
                ]
            },
            "DefaultCacheBehavior": {
                "TargetOriginId": mp_host,
                "ViewerProtocolPolicy": "redirect-to-https",
                "CachePolicyId": "08627262-05a9-4f76-9ded-b50ca2e3a84f",            # Hard-coded default policy
                "ResponseHeadersPolicyId": "60669652-455b-4ae9-85a4-c4c02393f86c"   # Hard-coded default policy
            },
            "Comment": id_segment,
            "Enabled": True
        })
        response = Utils.check_response(response)
        if response:
            print("CF Distribution create %s" % response['Distribution']['Id'])
        return response
