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

    def get_cf_distribution_config(self, cf_id):
        response = self.client.get_distribution_config(Id=cf_id)
        response = Utils.check_response(response)
        return response

    def update_cf_distribution(self, cf_id, dist_config, etag):
        response = self.client.update_distribution(Id=cf_id, DistributionConfig=dist_config, IfMatch=etag)
        response = Utils.check_response(response)
        return response

    def get_cf_status(self, cf_id):
        response = self.client.get_distribution(Id=cf_id)
        response = Utils.check_response(response)
        if response:
            return response['Distribution']['Status']
        return None

    def _send_delete(self, cf_id, etag):
        response = self.client.delete_distribution(Id=cf_id, IfMatch=etag)
        response = Utils.check_response(response)
        return response

    def delete_cf_distribution(self, cf_id):
        """
        Delete Cloudfront Distribution
        :param cf_id:
        :return:    None on error
                    "Disabling" when disable is processing
                    "Deleted" when delete success
        """
        # Step 1 get distribution enable state
        response = self.get_cf_distribution_config(cf_id)
        if not response:
            return None
        dist_config = response['DistributionConfig']
        etag = response['ETag']
        # Step 2 if enabled, disable
        if dist_config['Enabled']:
            dist_config['Enabled'] = False
            response = self.update_cf_distribution(cf_id, dist_config, etag)
            if not response:
                return None
        # Step 3 get distribution status
        response = self.get_cf_status(cf_id)
        if response is None:
            return None
        if response != "Deployed":
            return "Disabling"
        # Step 4 if deployed, delete
        response = self._send_delete(cf_id, etag)
        if response is None:
            return None
        return "Deleted"
