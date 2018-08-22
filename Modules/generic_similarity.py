from ontobio.ontol_factory import OntologyFactory
from ontobio.assoc_factory import AssociationSetFactory
from ontobio.assocmodel import AssociationSet

class GenericSimilarity(object):
    """
    Note: We should make afactory.create able to load from url's if the file has a web protocol in it
    Also, fmt should be assumed?
    """

    def __init__(self, ont:str, subject_category:str, object_category:str, taxon:str=None, file:str=None, fmt:str=None):
        """
        """
        ofactory = OntologyFactory()
        ontology = ofactory.create(ont, subject_category)

        afactory = AssociationSetFactory()

        self.associations = afactory.create(
            ontology=ontology,
            subject_category=subject_category,
            object_category=object_category,
            taxon=taxon,
            file=file,
            fmt=fmt
        )

    def compute_jaccard(self, input_curies):
        similarities = []

        for input_curie in input_curies:
            for subject_curie in self.associations.subject_label_map.keys():
                score = self.associations.jaccard_similarity(input_curie, subject_curie)

                if score > .7 and score < 1:
                    similarities.append({
                        'input_curie': input_curie,
                        'sim_hit_name': self.associations.label(subject_curie),
                        'sim_hit_curie': subject_curie,
                        'sim_score': score,
                    })

        return similarities
