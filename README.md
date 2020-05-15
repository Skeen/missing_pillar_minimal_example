# Steps to reproduce
1. Install salt-ssh
2. Create a server running sshd + python. Gain ssh access to it and note the IP
3. Replace `IP_HERE` in `config/roster` with the IP of the machine.
4. Verify pillar data with: `salt-ssh '*' pillar.items`, expected output is:
```
target:
    ----------
    example_key:
        example_value
```
5. Run the custom module with: `salt-ssh '*' application.test`, output is:
```
target:
    ----------
    Results:
        ----------
        __salt__:
            <salt.loader.LazyLoader object at 0x7fc362888b70>
        config.get_grain:
            salt-pillar-test
        config.get_master:
            default
        config.get_pillar:
            default
        dummy:
            cafebabe
        pillar.items_eval:
            ----------
        pillar.items_func:
            <function items at 0x7fc3627b90d0>
    retcode:
        0
```
Expected output under `pillar.items_eval` would be the output from step 4.

What can be seen is that grains are picked up with `config.get`, but master
configuration and pillars are not.
