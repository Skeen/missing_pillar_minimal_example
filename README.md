# Steps to reproduce
1. Install `salt-ssh`
2. Create a server running `sshd` + `python`. Gain SSH access to it and note the IP.
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
        __pillar__:
            ----------
        __salt__:
            <salt.loader.LazyLoader object at 0x7fc362888b70>
        config.get_grain:
            salt-pillar-test
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

What can be seen is that grains are picked up with `config.get`, but pillars
are not.

6. Running the custom module via a state: `salt-ssh '*' state.apply state`, yields:
```
target:
----------
          ID: pillar_test_state
    Function: module.run
        Name: application.test
      Result: True
     Comment: Module function application.test executed
     Started: 11:26:51.005461
    Duration: 38.598 ms
     Changes:
              ----------
              ret:
                  ----------
                  Results:
                      ----------
                      __pillar__:
                          ----------
                          example_key:
                              example_value
                      __salt__:
                          <salt.loader.LazyLoader object at 0x7f4d9111e4a8>
                      config.get_grain:
                          salt-master-test
                      config.get_pillar:
                          example_value
                      dummy:
                          cafebabe
                      pillar.items_eval:
                          ----------
                          example_key:
                              example_value
                      pillar.items_func:
                          <function items at 0x7f4d9104b378>
                  retcode:
                      0

Summary for target
------------
Succeeded: 1 (changed=1)
Failed:    0
------------
Total states run:     1
Total run time:  38.598 ms
```
And thus we have our pillar data.
