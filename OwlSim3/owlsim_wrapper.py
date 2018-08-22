import requests
import datetime

class PhenotypeSimilaritySearch(object):

    def __init__(self, endpoint='http://owlsim3.monarchinitiative.org/api'):
        """
        Initialize SimSearch
        """
        self.endpoint = endpoint
        self.results = None

    def search(self, phenotype_set, matcher='phenodigm'):
        """
        Given a phenotype set and a matcher, perform a phenotype search
        """
        phenotype_set = self.filter_blacklist_terms(phenotype_set)
        url = "{}/match/{}".format(self.endpoint, matcher)
        params = {
            'id': phenotype_set
        }
        response = requests.get(url=url, params=params)
        self.results = response.json()

    def get_results(self, type=None):
        """
        Subset the results to a particular type of matches
        """
        data = []
        curies = []

        for match in self.results['matches']:
            if type == 'gene':
                if 'NCBIGene' in match['matchId']:
                    data.append(match)
                    curies.append(match['matchId'])
            elif type == 'disease':
                if 'NCBIGene' not in match['matchId']:
                    data.append(match)
                    curies.append(match['matchId'])

        return {
            'data': data,
            'curies': curies
        }

    @staticmethod
    def filter_blacklist_terms(list, blacklist=['HP:0025023']):
        """
        Filter blacklist terms from list
        """
        filtered_list = [x for x in list if x not in blacklist]
        return filtered_list
