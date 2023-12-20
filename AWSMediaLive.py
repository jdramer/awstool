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

    @staticmethod
    def _ml_destinations(dest_id, mpc_id):
        return [{
            "Id": dest_id,
            "MediaPackageSettings": [{
                "ChannelId": mpc_id
            }]
        }]

    @staticmethod
    def _ml_encoder_settings(dest_id):
        return {
            "AudioDescriptions": [
              {
                "AudioSelectorName": "Default",
                "AudioTypeControl": "FOLLOW_INPUT",
                "CodecSettings": {
                  "AacSettings": {
                    "Bitrate": 192000,
                    "CodingMode": "CODING_MODE_2_0",
                    "InputType": "NORMAL",
                    "Profile": "LC",
                    "RateControlMode": "CBR",
                    "RawFormat": "NONE",
                    "SampleRate": 48000,
                    "Spec": "MPEG4"
                  }
                },
                "LanguageCodeControl": "FOLLOW_INPUT",
                "Name": "audio_1"
              },
              {
                "AudioSelectorName": "Default",
                "AudioTypeControl": "FOLLOW_INPUT",
                "CodecSettings": {
                  "AacSettings": {
                    "Bitrate": 192000,
                    "CodingMode": "CODING_MODE_2_0",
                    "InputType": "NORMAL",
                    "Profile": "LC",
                    "RateControlMode": "CBR",
                    "RawFormat": "NONE",
                    "SampleRate": 48000,
                    "Spec": "MPEG4"
                  }
                },
                "LanguageCodeControl": "FOLLOW_INPUT",
                "Name": "audio_2"
              },
              {
                "AudioSelectorName": "Default",
                "AudioTypeControl": "FOLLOW_INPUT",
                "CodecSettings": {
                  "AacSettings": {
                    "Bitrate": 128000,
                    "CodingMode": "CODING_MODE_2_0",
                    "InputType": "NORMAL",
                    "Profile": "LC",
                    "RateControlMode": "CBR",
                    "RawFormat": "NONE",
                    "SampleRate": 48000,
                    "Spec": "MPEG4"
                  }
                },
                "LanguageCodeControl": "FOLLOW_INPUT",
                "Name": "audio_3"
              },
              {
                "AudioSelectorName": "Default",
                "AudioTypeControl": "FOLLOW_INPUT",
                "CodecSettings": {
                  "AacSettings": {
                    "Bitrate": 128000,
                    "CodingMode": "CODING_MODE_2_0",
                    "InputType": "NORMAL",
                    "Profile": "LC",
                    "RateControlMode": "CBR",
                    "RawFormat": "NONE",
                    "SampleRate": 48000,
                    "Spec": "MPEG4"
                  }
                },
                "LanguageCodeControl": "FOLLOW_INPUT",
                "Name": "audio_4"
              }
            ],
            "OutputGroups": [
              {
                "Name": "HD",
                "OutputGroupSettings": {
                  "MediaPackageGroupSettings": {
                    "Destination": {
                      "DestinationRefId": dest_id
                    }
                  }
                },
                "Outputs": [
                  {
                    "AudioDescriptionNames": [
                      "audio_1"
                    ],
                    "CaptionDescriptionNames": [],
                    "OutputName": "1080p30",
                    "OutputSettings": {
                      "MediaPackageOutputSettings": {}
                    },
                    "VideoDescriptionName": "video_1080p30"
                  },
                  {
                    "AudioDescriptionNames": [
                      "audio_2"
                    ],
                    "CaptionDescriptionNames": [],
                    "OutputName": "720p30",
                    "OutputSettings": {
                      "MediaPackageOutputSettings": {}
                    },
                    "VideoDescriptionName": "video_720p30"
                  },
                  {
                    "AudioDescriptionNames": [
                      "audio_3"
                    ],
                    "CaptionDescriptionNames": [],
                    "OutputName": "480p30",
                    "OutputSettings": {
                      "MediaPackageOutputSettings": {}
                    },
                    "VideoDescriptionName": "video_480p30"
                  },
                  {
                    "AudioDescriptionNames": [
                      "audio_4"
                    ],
                    "CaptionDescriptionNames": [],
                    "OutputName": "240p30",
                    "OutputSettings": {
                      "MediaPackageOutputSettings": {}
                    },
                    "VideoDescriptionName": "video_240p30"
                  }
                ]
              }
            ],
            "TimecodeConfig": {
              "Source": "SYSTEMCLOCK"
            },
            "VideoDescriptions": [
              {
                "CodecSettings": {
                  "H264Settings": {
                    "AdaptiveQuantization": "HIGH",
                    "AfdSignaling": "NONE",
                    "Bitrate": 5000000,
                    "ColorMetadata": "INSERT",
                    "EntropyEncoding": "CABAC",
                    "FlickerAq": "ENABLED",
                    "ForceFieldPictures": "DISABLED",
                    "FramerateControl": "SPECIFIED",
                    "FramerateDenominator": 1,
                    "FramerateNumerator": 30,
                    "GopBReference": "ENABLED",
                    "GopClosedCadence": 1,
                    "GopNumBFrames": 3,
                    "GopSize": 60,
                    "GopSizeUnits": "FRAMES",
                    "Level": "H264_LEVEL_AUTO",
                    "LookAheadRateControl": "HIGH",
                    "NumRefFrames": 3,
                    "ParControl": "SPECIFIED",
                    "Profile": "HIGH",
                    "RateControlMode": "CBR",
                    "ScanType": "PROGRESSIVE",
                    "SceneChangeDetect": "ENABLED",
                    "Slices": 1,
                    "SpatialAq": "ENABLED",
                    "SubgopLength": "FIXED",
                    "Syntax": "DEFAULT",
                    "TemporalAq": "ENABLED",
                    "TimecodeInsertion": "DISABLED"
                  }
                },
                "Height": 1080,
                "Name": "video_1080p30",
                "RespondToAfd": "NONE",
                "ScalingBehavior": "DEFAULT",
                "Sharpness": 50,
                "Width": 1920
              },
              {
                "CodecSettings": {
                  "H264Settings": {
                    "AdaptiveQuantization": "HIGH",
                    "AfdSignaling": "NONE",
                    "Bitrate": 3000000,
                    "ColorMetadata": "INSERT",
                    "EntropyEncoding": "CABAC",
                    "FlickerAq": "ENABLED",
                    "ForceFieldPictures": "DISABLED",
                    "FramerateControl": "SPECIFIED",
                    "FramerateDenominator": 1,
                    "FramerateNumerator": 30,
                    "GopBReference": "ENABLED",
                    "GopClosedCadence": 1,
                    "GopNumBFrames": 3,
                    "GopSize": 60,
                    "GopSizeUnits": "FRAMES",
                    "Level": "H264_LEVEL_AUTO",
                    "LookAheadRateControl": "HIGH",
                    "NumRefFrames": 3,
                    "ParControl": "SPECIFIED",
                    "Profile": "HIGH",
                    "RateControlMode": "CBR",
                    "ScanType": "PROGRESSIVE",
                    "SceneChangeDetect": "ENABLED",
                    "Slices": 1,
                    "SpatialAq": "ENABLED",
                    "SubgopLength": "FIXED",
                    "Syntax": "DEFAULT",
                    "TemporalAq": "ENABLED",
                    "TimecodeInsertion": "DISABLED"
                  }
                },
                "Height": 720,
                "Name": "video_720p30",
                "RespondToAfd": "NONE",
                "ScalingBehavior": "DEFAULT",
                "Sharpness": 100,
                "Width": 1280
              },
              {
                "CodecSettings": {
                  "H264Settings": {
                    "AdaptiveQuantization": "HIGH",
                    "AfdSignaling": "NONE",
                    "Bitrate": 1500000,
                    "ColorMetadata": "INSERT",
                    "EntropyEncoding": "CABAC",
                    "FlickerAq": "ENABLED",
                    "ForceFieldPictures": "DISABLED",
                    "FramerateControl": "SPECIFIED",
                    "FramerateDenominator": 1,
                    "FramerateNumerator": 30,
                    "GopBReference": "ENABLED",
                    "GopClosedCadence": 1,
                    "GopNumBFrames": 3,
                    "GopSize": 60,
                    "GopSizeUnits": "FRAMES",
                    "Level": "H264_LEVEL_AUTO",
                    "LookAheadRateControl": "HIGH",
                    "NumRefFrames": 3,
                    "ParControl": "SPECIFIED",
                    "ParDenominator": 3,
                    "ParNumerator": 4,
                    "Profile": "MAIN",
                    "RateControlMode": "CBR",
                    "ScanType": "PROGRESSIVE",
                    "SceneChangeDetect": "ENABLED",
                    "Slices": 1,
                    "SpatialAq": "ENABLED",
                    "SubgopLength": "FIXED",
                    "Syntax": "DEFAULT",
                    "TemporalAq": "ENABLED",
                    "TimecodeInsertion": "DISABLED"
                  }
                },
                "Height": 480,
                "Name": "video_480p30",
                "RespondToAfd": "NONE",
                "ScalingBehavior": "STRETCH_TO_OUTPUT",
                "Sharpness": 100,
                "Width": 640
              },
              {
                "CodecSettings": {
                  "H264Settings": {
                    "AdaptiveQuantization": "HIGH",
                    "AfdSignaling": "NONE",
                    "Bitrate": 750000,
                    "ColorMetadata": "INSERT",
                    "EntropyEncoding": "CABAC",
                    "FlickerAq": "ENABLED",
                    "ForceFieldPictures": "DISABLED",
                    "FramerateControl": "SPECIFIED",
                    "FramerateDenominator": 1,
                    "FramerateNumerator": 30,
                    "GopBReference": "ENABLED",
                    "GopClosedCadence": 1,
                    "GopNumBFrames": 3,
                    "GopSize": 60,
                    "GopSizeUnits": "FRAMES",
                    "Level": "H264_LEVEL_AUTO",
                    "LookAheadRateControl": "HIGH",
                    "NumRefFrames": 3,
                    "ParControl": "SPECIFIED",
                    "ParDenominator": 3,
                    "ParNumerator": 4,
                    "Profile": "MAIN",
                    "RateControlMode": "CBR",
                    "ScanType": "PROGRESSIVE",
                    "SceneChangeDetect": "ENABLED",
                    "Slices": 1,
                    "SpatialAq": "ENABLED",
                    "SubgopLength": "FIXED",
                    "Syntax": "DEFAULT",
                    "TemporalAq": "ENABLED",
                    "TimecodeInsertion": "DISABLED"
                  }
                },
                "Height": 240,
                "Name": "video_240p30",
                "RespondToAfd": "NONE",
                "ScalingBehavior": "STRETCH_TO_OUTPUT",
                "Sharpness": 100,
                "Width": 320
              }
            ]
          }

    @staticmethod
    def _ml_input_attachments(mli_name, mli_id):
        return [{
            "InputAttachmentName": mli_name,
            "InputId": mli_id
        }]

    @staticmethod
    def _ml_input_spec():
        return {
            "Codec": "AVC",
            "MaximumBitrate": "MAX_10_MBPS",
            "Resolution": "HD"
        }

    def create_ml_channel(self, name, mpc_id, mli_name, mli_id):
        dest_id = "destid-" + name
        response = self.client.create_channel(ChannelClass='SINGLE_PIPELINE',
                                              Destinations=self._ml_destinations(dest_id, mpc_id),
                                              EncoderSettings=self._ml_encoder_settings(dest_id),
                                              InputAttachments=self._ml_input_attachments(mli_name, mli_id),
                                              InputSpecification=self._ml_input_spec(),
                                              LogLevel="WARNING",
                                              Name="mlc-"+name,
                                              RoleArn=self.config.medialive_role)
        response = Utils.check_response(response)
        if response:
            print("Created MLC %s" % response["Channel"]['Id'])
        return response

    def delete_ml_channel(self, mlc_id):
        response = self.client.delete_channel(ChannelId=mlc_id)
        response = Utils.check_response(response)
        if response:
            print("ML Channel Deleted")
        return response
