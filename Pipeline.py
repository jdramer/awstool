#! python3

"""Pipeline.py: Storage for pipeline data"""
import urllib.parse


class Pipeline(object):
    """
    Storage object for pipeline data
    """

    def __init__(self):
        self.mli_id = None
        self.mli_rtmp_url = None
        self.mli_name = None
        self.mlc_id = None
        self.mpc_id = None
        self.mpoe_id = None
        self.mpoe_url = None
        self.cf_id = None
        self.cf_domain = None
        self.cf_url = None

    def load_mli_create_response(self, response):
        if not response:
            return
        inp = response["Input"]
        self.mli_id = inp["Id"]
        self.mli_name = inp["Name"]
        self.mli_rtmp_url = inp["Destinations"][0]["Url"]

    def load_mlc_create_response(self, response):
        if not response:
            return
        channel = response["Channel"]
        self.mlc_id = channel["Id"]

    def load_mpc_create_response(self, response):
        if not response:
            return
        self.mpc_id = response["Id"]

    def load_mpoe_create_response(self, response):
        if not response:
            return
        self.mpoe_id = response["Id"]
        self.mpoe_url = response["Url"]

    def load_cf_create_response(self, response):
        if not response:
            return
        dist = response['Distribution']
        self.cf_id = dist['Id']
        self.cf_domain = dist['DomainName']
        self.cf_url = urllib.parse.urlparse(self.mpoe_url)._replace(netloc=self.cf_domain).geturl()

    def show_pipeline_objects(self):
        print("Clean up with\npython awstool.py --delete %s %s %s %s %s" %
              (self.mpc_id, self.mpoe_id, self.cf_id, self.mli_id, self.mlc_id))

    def show_pipeline_ready(self):
        print("==========================================")
        print("Congratulations! Pipeline is ready to use.")
        print("Connect encoder to %s" % self.mli_rtmp_url)
        print("View stream at %s" % self.cf_url)
        print("==========================================")
        print("")
        self.show_pipeline_objects()
