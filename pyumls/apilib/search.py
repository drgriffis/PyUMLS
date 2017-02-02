#################################################################################
# Original source from NLM UMLS API examples
# Modified by: Denis Griffis
#
# see https://documentation.uts.nlm.nih.gov/rest/search/index.html for full docs
# on the /search endpoint
#
# version - example 2015AA
# string - example "diabetic foot"
#################################################################################

from .auth import *
import requests
import json

def search(string, apikey, version='2016AB', max_pages=5, **extra_args):
    '''Run a search query on the UMLS REST API

    Parameters:
        string    -- the string to search for (e.g., "diabetic foot")
        apikey    -- account-linked API key for authentication
        version   -- UMLS release to search (default '2016AB')
        max_pages -- maximum number of result pages to fetch (default 5; None for unlimited)
        **        -- additional keyword args are passed into the API query
    '''
    uri = "https://uts-ws.nlm.nih.gov"
    content_endpoint = "/rest/search/"+version

    # get authentication granting ticket for the session
    AuthClient = Authentication(apikey)
    tgt = AuthClient.gettgt()
    page_number=0

    results = []
    while True:
        # break option 1: hit page cap
        if (max_pages is None) or page_number >= max_pages: break
        # generate a new service ticket for each page if needed
        ticket = AuthClient.getst(tgt)
        
        page_number += 1
        query = { 'string':string, 'ticket':ticket, 'pageNumber':page_number }
        for (k,v) in extra_args.items():
            query[k] = v
        #query['includeObsolete'] = 'true'
        #query['includeSuppressible'] = 'true'
        #query['returnIdType'] = "sourceConcept"
        #query['sabs'] = "SNOMEDCT_US"

        r = requests.get(uri+content_endpoint,params=query)
        r.encoding = 'utf-8'
        items = json.loads(r.text)
        jsonData = items["result"]
        
        # break option 2: no more results
        if jsonData["results"][0]["ui"] == "NONE":
            break
        else:
            results.extend(jsonData["results"]);
    return results
