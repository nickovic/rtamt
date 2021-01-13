# online monitors matlab simulink

This directory demonstrates the integration of RTAMT online monitors to MATLAB/Simulink.

The monitors are integrated by using the MATLAB Lever 2 S-Function online_monitor.m, which is used to create a new S-Function simulink block online_monitor.

The main MATLAB script to start the simulation with the monitor is online_monitoring_demo.m.

The script can also be executed from the shell (Unix) with the following command:

```bash
matlab -nodesktop -nosplash -r "run('<RTAMT_INSTALL_DIR>/rtamt/examples/online_monitors_matlab_simulink/online_monitoring_demo.m');quit;"
```
