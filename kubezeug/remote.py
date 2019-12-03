from distributed import Client
from functools import wraps

def run_on(cluster):
    client = Client(cluster, set_as_default=False)
    def _run(fn):
        @wraps(fn)
        def _run_with_args(*args, **kwargs):
            result = client.run(fn, *args, **kwargs)
            client.close()
            return result
        return _run_with_args
    return _run

