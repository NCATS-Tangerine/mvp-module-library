from OwlSim3.owlsim_wrapper import PhenotypeSimilaritySearch
from Modules.generic_similarity import GenericSimilarity

class PhenotypeSimilarity(GenericSimilarity):

    def __init__(self):
        self.phenotype_set = None

    def load_phenotype_set(self, phenotype_set):
        self.phenotype_set = phenotype_set

    def similarity_search(self, return_type):
        sim_search = PhenotypeSimilaritySearch()
        sim_search.search(phenotype_set=self.phenotype_set)
        results = sim_search.get_results(return_type)
        return results
