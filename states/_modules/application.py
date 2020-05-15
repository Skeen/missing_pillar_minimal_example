import salt.utils

__virtualname__ = 'application'

def __virtual__():
    return __virtualname__

def test():
    ret = {'retcode': 0}
    results = ret.setdefault('Results', {})
    results['dummy'] = 'cafebabe'
    results['__salt__'] = __salt__
    results['__pillar__'] = __pillar__
    results['pillar.items_func'] = __salt__['pillar.items']
    results['pillar.items_eval'] = __salt__['pillar.items']()
    #results['config.items_func'] = __salt__['config.items']
    #results['config.items_eval'] = __salt__['config.items']()
    results['config.get_grain'] = __salt__['config.get']('host', "default")
    results['config.get_pillar'] = __salt__['config.get']('example_key', "default")
    return ret
