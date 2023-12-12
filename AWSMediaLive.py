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

    def create_ml_input(self, name):
        response = self.client.create_input(Destinations=[{"StreamName": "mlia-"+name+"/mlii-"+name}],
                                            Name="mli-"+name,
                                            Type="RTMP_PUSH",
                                            InputSecurityGroups=[self.config.input_security_group])
        response = Utils.check_response(response)
        if response:
            print("Created MLI %s" % response["Input"]['Id'])
        return response

    def delete_ml_input(self, input_id):
        response = self.client.delete_input(InputId=input_id)
        response = Utils.check_response(response)
        if response:
            print("ML Input Deleted")
        return response
