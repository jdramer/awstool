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
        response = self.client.describe_channel(Id=mp_channel_id)
        response = Utils.check_response(response)
        if response:
            print("MP Channel %s Created %s" % (mp_channel_id, response['CreatedAt']))
        return response

    def create_mp_channel(self, id_segment):
        response = self.client.create_channel(Id="mpc-"+id_segment)
        response = Utils.check_response(response)
        if response:
            print("MP Channel created %s" % response['Id'])
        return response

    def delete_mp_channel(self, mpc_id):
        response = self.client.delete_channel(Id=mpc_id)
        response = Utils.check_response(response)
        if response:
            print("MP Channel Deleted")
        return response

    def create_mp_endpoint(self, id_segment):
        mpc_id = "mpc-"+id_segment
        mpoe_id = "mpoe-"+id_segment
        manifest_name = "index-"+id_segment
        response = self.client.create_origin_endpoint(
            Id=mpoe_id, ChannelId=mpc_id, ManifestName=manifest_name,
            StartoverWindowSeconds=172800,
            HlsPackage={
                'PlaylistType': 'EVENT',
                'PlaylistWindowSeconds': 60,
                'SegmentDurationSeconds': 6
            })
        response = Utils.check_response(response)
        if response:
            print("MP Endpoint created %s" % response['Id'])
        return response

    def delete_mp_endpoint(self, mpoe_id):
        response = self.client.delete_origin_endpoint(Id=mpoe_id)
        response = Utils.check_response(response)
        if response:
            print("MP Endpoint Deleted")
        return response
