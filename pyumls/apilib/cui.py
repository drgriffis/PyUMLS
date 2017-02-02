#################################################################################
# Original source from NLM UMLS API examples
# Modified by: Denis Griffis
#
# see https://documentation.uts.nlm.nih.gov/rest/concept/index.html for full docs
# on the concept portion of the /content endpoint
#
# version - example 2015AA
# cui - example "C0020538"
#################################################################################

from .auth import *
import requests
import json

def getByCUI(cui, apikey, version='2016AB'):
    '''
    '''
    uri = "https://uts-ws.nlm.nih.gov"
    content_endpoint = "/rest/content/"+version+"/CUI/"+cui

    # get authentication granting ticket for the session
    AuthClient = Authentication(apikey)
    tgt = AuthClient.gettgt()

    # generate a new service ticket
    ticket = AuthClient.getst(tgt)

    query = { 'ticket':ticket }

    r = requests.get(uri+content_endpoint,params=query)
    r.encoding = 'utf-8'
    items = json.loads(r.text)
    jsonData = items["result"]

    return jsonData
