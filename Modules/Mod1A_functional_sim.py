from MyGene.mygene_client import QueryMyGene
from ontobio.ontol_factory import OntologyFactory
from ontobio.io.gafparser import GafParser
from ontobio.assoc_factory import AssociationSetFactory
from .generic_similarity import GenericSimilarity

URI = 'http://geneontology.org/gene-associations/goa_{group}.gaf.gz'
DEFAULT_GROUP = 'human'

class FunctionalSimilarity(GenericSimilarity):
    def __init__(self, ont='go', subject_category='gene', object_category='function', file=None, fmt='gaf', group=None):
        if group != None:
            file = URI.format(group=group)

        if file == None:
            file = URI.format(group=DEFAULT_GROUP)

        super(FunctionalSimilarity, self).__init__(
            ont=ont,
            subject_category=subject_category,
            object_category=object_category,
            file=file,
            fmt=fmt
        )

        self.symbol_map = {}
        self.identifier_map = {}

    def load_gene_set(self, gene_set):

        for gene in gene_set:
            mg = QueryMyGene()
            gene_dat = mg.query_mygene(curie=gene)
            ukb = QueryMyGene.parse_uniprot(gene_dat)
            uniprotkb = 'UniProtKB:{}'.format("".join(ukb))

            self.symbol_map[uniprotkb] = gene_dat['symbol']
            self.identifier_map[uniprotkb] = gene

    def compute_similarity(self):
        uniprotkb_gene_set = self.identifier_map.keys()
        results = self.compute_jaccard(uniprotkb_gene_set)

        for result in results:
            input_curie = result['input_curie']
            result['input_curie'] = self.identifier_map[input_curie]
            result['input_name'] = self.symbol_map[input_curie]

        return results
