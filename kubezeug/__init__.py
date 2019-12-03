import logging
from .remote import run_on
from .cluster import create_cluster
try:
    import tensorflow
    from .kube_resolver import KubernetesClusterResolver
except:
    logging.warning("tensorkube: No installation of tensorflow found. \
                     Some APIs will not be available.")

__version__ = '0.0.1'

