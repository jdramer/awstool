#! python3

"""awsms.py: Tool for automating AWS pipeline creation"""
import argparse

import AWSConfig
import AWSMediaPackage
import Pipeline
import Utils


def create_pipeline(config, id_segment):
    # Create Pipeline storage
    pipeline = Pipeline.Pipeline()

    # Create MediaPackage Channel

    # Create MediaPackage Endpoint

    # Create Cloudfront object

    # Create MediaLive Input

    # Create MediaLive Channel

    # Start MediaLive Channel

    # Wait for MediaLive to enter running state

    # Wait for Cloudfront to become Deployed

    # Dump pipeline that was created
    pipeline.show_pipeline_objects()


def delete_pipeline(config, mpc_id, mpoe_id, cf_id, mli_id, mlc_id):
    # Stop MediaLive Channel and delete

    # Delete MediaLive Input

    # Delete MediaPackage Endpoint

    # Delete MediaPackage Channel

    # Delete Cloudfront
    pass


if __name__ == "__main__":
    # Handle script arguments
    parser = argparse.ArgumentParser(
        prog="AWSTool",
        description="AWS Media Services Pipeline Tool"
    )
    parser.add_argument('--create', metavar='ID',
                        help='Create a pipeline using ID in names')
    parser.add_argument('--delete', nargs=5, metavar=('MPC_ID', 'MPOE_ID', 'CF_ID', 'MLI_ID', 'MLC_ID'),
                        help='Delete a pipeline with the specified IDs. Use None for any that does not exist')
    args = parser.parse_args()

    # Set up config
    config = AWSConfig.AWSConfig()
    config.init_from_ini("jramer.ini", "us-west-2")

    if args.create:
        create_pipeline(config, args.create)
    if args.delete:
        delete_pipeline(config, *args.delete)
