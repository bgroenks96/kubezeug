from dask_kubernetes import KubeCluster

def create_cluster(image='daskdev/dask:latest', imagePullPolicy='IfNotPresent', nthreads=2, death_timeout=60,
                   labels=dict(), name='dask', env=dict(), cpu_limit='2', memory_limit='6G', num_gpu=0,
                   restartPolicy='Never'):
    cluster_spec = {
        'kind': 'Pod',
        'spec': {
            'restartPolicy': restartPolicy, 
            'containers': [{
                'image': image,
                'imagePullPolicy': imagePullPolicy,
                'args': ['dask-worker', '--nthreads', str(nthreads), '--no-bokeh', '--memory-limit', memory_limit,
                         '--death-timeout', death_timeout],
                'name': name,
                'env': [{'name': key, 'value': value} for key, value in env],
                'resources': {
                    'limits': {
                        'cpu': cpu_limit,
                        'memory': memory_limit,
                    }
                }
            }]
        }
    }
    if labels:
        cluster_spec['metadata'] = {'labels': labels}
    if num_gpu > 0:
        cluster_spec['spec']['containers'][0]['resources']['limits']['nvidia.com/gpu'] = str(num_gpu)
    return KubeCluster.from_dict(cluster_spec)

