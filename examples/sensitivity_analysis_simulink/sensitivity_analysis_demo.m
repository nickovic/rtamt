% PROGRAM: Sensitivity analysis demo
% -------------------------------------------------------------
% Simulation of 16 aircraft model behaviors
% Input signals: 4 amplitudes x 4 frequencies
% and offline monitoring of its STL requirement
% Plot of a sensitivity heat map
% -------------------------------------------------------------
% Created:  20-01-2019
% Author:   Dejan Nickovic

clear;
warning ('off','all');

disp('Setting up the simulation environment');

% Set up simulation start and end time
start_time = 0;
stop_time = 10;

% Simulation sampling frequency
samp_freq = 0.01;

% Setup model environment
model_path = 'model/';
model_name_wo_ext = 'sf_aircraft_fault';
model_ext = '.slx';

% Load the model
system = load_system([model_path, model_name_wo_ext, model_ext]);

% Set the simulation environment
set_param(system, 'Solver', 'ode4', 'StopTime', '10', ...
    'ReturnWorkspaceOutputs', 'on');

% Set up the input (pilot command) parameters:
% Amplitude and frequency of the input
input_name = strcat(model_name_wo_ext, '/Pilot Command');
freq = '0.2';
amp = '1';

for(i=1:4)
    for(j=1:4)
        freq = 0.2*i;
        amp = 1+(0.25*(j-1));
        
        set_param(input_name, 'Frequency', num2str(freq), 'Amplitude', num2str(amp));
        
        disp(['Simulating the model with frequency ', num2str(freq), ...
            ' and amplitude ', num2str(amp)]);
        
        % Simulate the model
        simData = sim(model_name_wo_ext, 'SaveTime', 'on', 'TimeSaveName', 'tout',...
                     'SaveState', 'on', 'StateSaveName', 'xoutNew',...
                     'SaveOutput', 'on', 'OutputSaveName', 'youtNew', ...
                     'SignalLogging', 'on', 'SignalLoggingName', 'logsout');
        out(i,j) = simData.get('logsout');          
    end
end

disp('Simulation done.');

save_system(system);
close_system(system);

counter = 1;
for(i=1:4)
    for(j=1:4)
        disp(['Monitoring the specification phi on simulation trace ', num2str(counter)]);
        rob = monitor (out(i,j));
        disp(['phi robustness for trace ', num2str(counter), ': ', num2str(min(rob))]);
        R(i,j) = rob;
        counter = counter + 1;
    end
end

ylab = [0.2 0.4 0.8 1];
xlab = [1 1.25 1.5 1.75];

color_map(1:150,1) = linspace(1, 1, 150);
color_map(1:150,2) = linspace(0, 1, 150);
color_map(1:150,3) = linspace(0, 1, 150);

color_map(151:200,1) = linspace(1, 0, 50);
color_map(151:200,2) = linspace(1, 1, 50);
color_map(151:200,3) = linspace(1, 0, 50);


color_std = [1 0 0; 0 1 0];
hm_std = heatmap(xlab, ylab, R, 'ColorMap', color_map, 'XLabel', 'Amplitude', 'YLabel', 'Frequency', 'FontSize', 12);
title('Sensitivity of phi to input frequency and amplitude');
set(gcf,'color','w');



      
