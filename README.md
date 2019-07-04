# NCATS Translator mvp-module-library

The National Center for Advancing Translational Sciences (NCATS) is funding a 
[project called "Translator"](https://ncats.nih.gov/translator/projects) 
to develop cyberinfrastructure for biomedical knowledge integration.

One key objective is to develop a platform for specifying and running computational workflows connecting diverse 
biomedical data types (diseases, genes, drugs) with one another, to identify novel therapeutic 
options for the treatment of various medical conditions. Contributing to this goal is a set of bioinformatics modules 
which serve as building blocks for such workflows. Some of these modules are aggregated and published in this package,
for reuse in the project's _"minimal viable product"_ application(s).

### Installation

This package is published on PyPI (https://pypi.org/project/mvp-module-library/) and can be installed using pip: 
```
pip install mvp-module-library
```

As always, it's useful to have a separate Python virtual environment for your project:

```
virtualenv -p python3.6 venv
source venv/bin/activate
pip install mvp-module-library
```

### Usage Example

```
>>> from pprint import pprint
>>> from BioLink.biolink_client import BioLinkWrapper
>>> b = BioLinkWrapper()
>>> pprint(b.get_obj('MONDO:0005148'))
{'association_counts': None,
 'categories': ['disease'],
 'consider': None,
 'deprecated': None,
 'description': 'A type of diabetes mellitus that is characterized by insulin '
                'resistance or desensitization and increased blood glucose '
                'levels. This is a chronic disease that can develop gradually '
                'over the life of a patient and can be linked to both '
                'environmental factors and heredity.',
 'id': 'MONDO:0005148',
 'label': 'type 2 diabetes mellitus',
 'replaced_by': None,
 'synonyms': [{'pred': 'synonym', 'val': 'adult-onset diabetes', 'xrefs': None},
              {'pred': 'synonym',
               'val': 'diabetes mellitis type II',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'type II diabetes mellitus',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'type 2 diabetes mellitus non-insulin dependent',
               'xrefs': None},
              {'pred': 'synonym', 'val': 'diabetes, type 2', 'xrefs': None},
              {'pred': 'synonym', 'val': 'adult onset diabetes', 'xrefs': None},
              {'pred': 'synonym',
               'val': 'non-insulin dependent diabetes',
               'xrefs': None},
              {'pred': 'synonym', 'val': 'type II diabetes', 'xrefs': None},
              {'pred': 'synonym', 'val': 'type 2 diabetes', 'xrefs': None},
              {'pred': 'synonym',
               'val': 'T2DM - type 2 diabetes mellitus',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'non-insulin-dependent diabetes mellitus',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'non-insulin dependent diabetes mellitus',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'type 2 diabetes mellitus',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'noninsulin dependent diabetes',
               'xrefs': None},
              {'pred': 'synonym',
               'val': 'diabetes mellitis type 2',
               'xrefs': None},
              {'pred': 'synonym', 'val': 'NIDDM', 'xrefs': None}],
 'taxon': {'id': None, 'label': None},
 'types': None,
 'xrefs': None}
```
