%% Fault Detection Control Logic in an Aircraft Elevator Control System
% 
% This example shows how to design a fault detection,
% isolation, and recovery (FDIR) application for a pair of aircraft
% elevators with redundant actuators. The fault detection control logic
% used in this model is the same that is used in the Avionics subsystem of
% the Aerospace Blockset(TM) example entitled "NASA HL-20 with Optional
% FlightGear Interface."

% Copyright 2009-2012 The MathWorks, Inc.
%%
%
bdclose all;
mdl = 'sf_aircraft';
open_system(mdl);

rt = sfroot;
machine = rt.find('-isa','Stateflow.Machine','Name',mdl);
ModeLogicChart = machine.find('-isa','Stateflow.Chart','Name','Mode Logic');
ModeLogicChart.visible = 0;
%%
% *Figure 1: Top level of aircraft elevator control system model*
%% Description of Elevator Control System
%
% A typical aircraft has two elevators attached on the horizontal tails
% (one on each side of the fuselage). There are a number of redundant parts
% in the system to enhance safety of the aircraft. 
%% 
% 
imshow('sf_aircraft_FDIR_overview.png')
set(gcf,'NumberTitle','off','Toolbar','none','MenuBar','none')
%%
% *Figure 2: Schematic showing how the components of the elevator system
% are connected to one another*
%%
% For example, as shown in Figure 2, there are:
%%
% * Two independent hydraulic actuators per elevator (four total)
% * Three separate hydraulic circuits to drive the actuators
% * Two primary flight control units (PFCU)
% * Two control modules per actuator: full range control law and limited /
% reduced range control law
%
%% Fault Detection Control Logic for Elevator Control System
ModeLogicChart.visible = 1;
%%
% *Figure 3: Actuator mode logic for fault detection*
%%
% Each outer actuator has a dedicated hydraulic circuit, whereas the inner
% actuators share one hydraulic circuit.  Each actuator can be in either
% one of five modes: Passive, Standby, Active, Off, and Isolated.  By
% default, the outer actuators are in the Active mode, and the inner
% actuators are in the Standby mode. If a failure is detected in the outer
% actuators or in the hydraulic circuits that are connected to them, the
% fault detection system responds accordingly to maintain stability by
% turning the outer actuators off and activating the inner actuators.
%
%% Failure Definition
% If the aircraft is flying perfectly level, then the actuator position
% should maintain a constant value. If the position of an actuator
% increases or decreases by 10 cm from this zero point, then the fault
% detection system registers a failure in that actuator. The fault
% detection system also registers a failure if the change in actuator
% position is very rapid (i.e., the position changes at least 20 cm in 0.01
% seconds).
%
% Similarly, the fault detection system registers a fault in one of the
% hydraulic circuits if the pressure is out-of-bounds or if the pressure
% changes very rapidly. In this example, the fault detection system checks
% that the pressure in the hydraulic circuit is between 500 kPA and 2 MPa,
% and that the pressure changes no more than 100 kPa in 0.01 seconds.
%
%% Injecting Failures Into Fault Detection System
%
sf_aircraft_failures;
%%
% *Figure 4: GUI used to inject failures into the system*
%%
% A separate GUI (shown in Figure 4) that was created in GUIDE is used to inject
% failures into the fault detection systems for both the hydraulic circuits and the actuators.  By
% checking or unchecking boxes and pressing the Update button on the GUI,
% custom MATLAB(R) code runs as an intermediary between the
% GUI and the Simulink(R) model.  For example, when checking the H1 box and
% pressing the Update button to inject a failure into hydraulic circuit 1,
% the following custom MATLAB code is evaluated:
%%
% |% Define H1_fail Constant block location and get current value|
%
% |blockname=[mname '/Signal conditioning '...|
%
% |'and failures /Hydraulic Pressures/Measured ',char(10),...|
%
% |'Hydraulic system 1 ',...|
%
% |'pressures/Hydraulic pressure/H1_fail'];|
%
% |val=get(handles.H1,'Value');|
%
% |% Change value of H1_fail Constant block from 0 to 1 or from 1 to 0.|
%
% |if val|
%
%   set_param(blockname,'value','1');
%
% |else|
%
%   set_param(blockname,'value','0');
%
% |end|
%%
% This effectively turns on a switch within the Signal conditioning
% subsystem so that the fault detection system registers a a fault in
% hydraulic circuit 1.
blockname=[mdl '/Signal conditioning '...
'and failures /Hydraulic Pressures/Measured ',char(10),...
'Hydraulic system 1 ',...
'pressures/Hydraulic pressure/H1_fail'];
set_param(blockname,'value','1');
open_system([mdl '/Signal conditioning '...
'and failures /Hydraulic Pressures/Measured ',char(10),...
'Hydraulic system 1 ',...
'pressures/Hydraulic pressure']);
%%
% *Figure 5: Switch that injects a failure into hydraulic circuit #1 if
% value of Constant block H1_fail does not equal 0*
%% Responding to Failures
% Stateflow(R) responds to failures in the hydraulic circuits and actuators
% using truth table functions, event broadcasting, and control logic.  As
% an example, if the fault detection system registers a failure in hydraulic circuit 1 and no other
% failures occur, the L_switch truth table function evaluates Decision D1
% as true and performs Action 2, which is to turn off the left outer
% actuator.  This event is broadcast to the LO state, where the left outer
% actuator turns off.  After this occurs, an event is broadcast from the LO
% state to the LI state so that the left inner actuator is activated.  The
% right inner actuator is then activated since the left inner actuator is
% also active.  When this happens, an event is sent from the RI state to
% the RO state to place the right outer actuator on standby.  Thus, after
% the fault detection systems registers a failure in hydraulic circuit 1, the left outer actuator is turned
% off, the right outer actuator is placed on standby, and the inner
% actuators are activated.
%
%% Isolating Actuators When Fault Detection System Registers Failures
% When the fault detection system registers a failure occurs in one of the
% actuators, that actuator can no longer be activated. This is represented
% in the state chart by adding an Isolated state that contains no outgoing
% transitions.  Therefore, once an actuator enters the Isolated state, it
% remains in the Isolated state.
%
%% Recovering from Failures
% A recovery mechanism has also been placed in the fault detection,
% isolation and recovery control logic in case a failed system comes back
% online.  For example, if the fault detection system no longer detects
% failures in hydraulic circuit 1, the condition !u.low_press[0] is true,
% and the LO state can transition from the Off state to the Standby state.
% That way, if the fault detection system registers a failure occurs in
% another system, such as the left inner actuator, then the left outer
% actuator can be activated.
%
%% References 
% Pieter J. Mosterman and Jason Ghidella, "Model Reuse for the Training
% of Fault Scenarios in Aerospace," in _Proceedings of the AIAA(R) Modeling and
% Simulation Technologies Conference_, CD-ROM, paper 2004-4931, August 16 -
% 19, Rhode Island Convention Center, Providence, RI, 2004.
%%
% Jason R. Ghidella and Pieter J. Mosterman, "Applying Model-Based Design
% to a Fault Detection, Isolation, and Recovery System," in _Military
% Embedded Systems_, Summer, 2006.
