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
    mp = AWSMediaPackage.AWSMediaPackage(config)
    mpc_resp = mp.create_mp_channel(id_segment)
    if not mpc_resp:
        return
    pipeline.load_mpc_create_response(mpc_resp)
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
    mp = AWSMediaPackage.AWSMediaPackage(config)
    if mpc_id and mpc_id != "None":
        mp.delete_mp_channel(mpc_id)

    # Delete Cloudfront


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
