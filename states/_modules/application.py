import salt.utils

__virtualname__ = 'application'

def __virtual__():
    return __virtualname__

def test():
    ret = {'retcode': 0}
    results = ret.setdefault('Results', {})
    results['dummy'] = 'cafebabe'
    results['__salt__'] = __salt__
    results['pillar.items_func'] = __salt__['pillar.items']
    results['pillar.items_eval'] = __salt__['pillar.items']()
    return ret
