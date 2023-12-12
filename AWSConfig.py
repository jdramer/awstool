#! python3

"""AWSConfig.py: Configuration loader for AWS tool"""

import sys
import configparser
import boto3


class AWSConfig(object):
    """
    AWSConfig
    """

    def __init__(self):
        self.aws_access = ""
        self.aws_secret = ""
        self.aws_region = ""
        self.medialive_role = ""
        self.input_security_group = ""
        self.session = None

    def init_from_ini(self, ini_filename, ini_section):
        config = configparser.ConfigParser()
        config.read(ini_filename)

        if ini_section not in config.sections():
            print("Section %s not found in" % ini_section, file=sys.stderr)
            sys.exit(1)

        self.aws_access = config[ini_section]["AWS_ACCESS"]
        self.aws_secret = config[ini_section]["AWS_SECRET"]
        self.aws_region = config[ini_section]["AWS_REGION"]
        self.medialive_role = config[ini_section]["MEDIALIVE_ROLE"]
        self.input_security_group = config[ini_section]["INPUT_SECURITY_GROUP"]

        self.session = boto3.Session(aws_access_key_id=self.aws_access,
                                     aws_secret_access_key=self.aws_secret,
                                     region_name=self.aws_region)
