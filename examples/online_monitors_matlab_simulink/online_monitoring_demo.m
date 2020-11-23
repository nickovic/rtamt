% PROGRAM: Online monitoring demo
% -------------------------------------------------------------
% Simulation of the aircraft monitor with
% STL online monitor implemented as an S-function
% using rtamt library
% -------------------------------------------------------------
% Created:  20-01-2019
% Author:   Dejan Nickovic

clear;
warning ('off','all');

disp('Setting up the simulation environment');

% Set up simulation start and end time
start_time = 0;
stop_time = 10000;

% Simulation sampling frequency
samp_freq = 0.01;

% Setup model environment
model_path = '';
model_name_wo_ext = 'sf_aircraft_fault_with_monitor';
model_ext = '.slx';

% Load the model
system = load_system([model_path, model_name_wo_ext, model_ext]);

% Set the simulation environment
set_param(system, 'Solver', 'ode4', 'StopTime', '10', ...
    'ReturnWorkspaceOutputs', 'on');

% Set up the input (pilot command) parameters:
% Amplitude and frequency of the input
input_name = strcat(model_name_wo_ext, '/pc');
freq = '0.2';
amp = '1';

     
set_param(input_name, 'Frequency', num2str(freq), 'Amplitude', num2str(amp));
        
disp(['Simulating the model with frequency ', num2str(freq), ...
            ' and amplitude ', num2str(amp)]);
        
        % Simulate the model
simData = sim(model_name_wo_ext, 'SaveTime', 'on', 'TimeSaveName', 'tout',...
                     'SaveState', 'on', 'StateSaveName', 'xoutNew',...
                     'SaveOutput', 'on', 'OutputSaveName', 'youtNew', ...
                     'SignalLogging', 'on', 'SignalLoggingName', 'logsout');

disp('Simulation done.');

save_system(system);
close_system(system);

      
