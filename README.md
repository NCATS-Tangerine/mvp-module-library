# mvp-module-library
A collection of modules for executing MVP Workflows

### Installation

This package is published on PyPI (https://pypi.org/project/mvp-module-library/) and can be installed using pip: `pip install mvp-module-library`

As always, it's useful to have a separate virtual environment for your project:

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

### Publishing to PyPI

The `publish` command in the [Makefile](Makefile) will prompt for a username and password, and then publish this package to PyPI. Make sure to increment the version number in [setup.py](setup.py) before publishing a new version.
