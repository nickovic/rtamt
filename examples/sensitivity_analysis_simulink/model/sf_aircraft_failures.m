function varargout = sf_aircraft_failures(varargin)
% SF_AIRCRAFT_FAILURES MATLAB code file for failures.fig
%      SF_AIRCRAFT_FAILURES, by itself, creates a new SF_AIRCRAFT_FAILURES or raises the existing
%      singleton*.
%
%      H = SF_AIRCRAFT_FAILURES returns the handle to a new SF_AIRCRAFT_FAILURES or the handle to
%      the existing singleton*.
%
%      SF_AIRCRAFT_FAILURES('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SF_AIRCRAFT_FAILURES.M with the given input arguments.
%
%      SF_AIRCRAFT_FAILURES('Property','Value',...) creates a new SF_AIRCRAFT_FAILURES or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before failures_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to failures_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help failures

% Last Modified by GUIDE v2.5 22-Dec-2003 10:19:06

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @sf_aircraft_failures_OpeningFcn, ...
                   'gui_OutputFcn',  @sf_aircraft_failures_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin & isstr(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before sf_aircraft_failures is made visible.
function sf_aircraft_failures_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to sf_aircraft_failures (see VARARGIN)

% Choose default command line output for sf_aircraft_failures
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes sf_aircraft_failures wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = sf_aircraft_failures_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in H1.
function H1_Callback(hObject, eventdata, handles)
% hObject    handle to H1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in H2.
function H2_Callback(hObject, eventdata, handles)
% hObject    handle to H2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in H3.
function H3_Callback(hObject, eventdata, handles)
% hObject    handle to H3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in LO_pos_fail.
function LO_pos_fail_Callback(hObject, eventdata, handles)
% hObject    handle to LO_pos_fail (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in LI_pos_fail.
function LI_pos_fail_Callback(hObject, eventdata, handles)
% hObject    handle to LI_pos_fail (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in RI_pos_fail.
function RI_pos_fail_Callback(hObject, eventdata, handles)
% hObject    handle to RI_pos_fail (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in RO_pos_fail.
function RO_pos_fail_Callback(hObject, eventdata, handles)
% hObject    handle to RO_pos_fail (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Untitled_1_Callback(hObject, eventdata, handles)
% hObject    handle to Untitled_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Untitled_2_Callback(hObject, eventdata, handles)
% hObject    handle to Untitled_2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes on button press in Inject_failure.
function Inject_failure_Callback(hObject, eventdata, handles)
% hObject    handle to Inject_failure (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% read current value of each check box, and
% update all failure injections in the Simulink model

% Get model name
mname=gcs;
num=findstr(mname,'/');
if ~isempty(num)
    mname=mname(1:num-1);
end

% H1
blockname=[mname '/Signal conditioning '...
'and failures /Hydraulic Pressures/Measured ',char(10),...
'Hydraulic system 1 ',...
'pressures/Hydraulic pressure/H1_fail'];
val=get(handles.H1,'Value');

if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

% H2
blockname=[mname '/Signal conditioning '...
'and failures /Hydraulic Pressures/Measured ',char(10),...
'Hydraulic system 2 ',...
'pressures/Hydraulic pressure/H2_fail'];
val=get(handles.H2,'Value');

if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

%H3
blockname=[mname '/Signal conditioning '...
'and failures /Hydraulic Pressures/Measured ',char(10),...
'Hydraulic system 3 ',...
'pressures/Hydraulic pressure/H3_fail'];
val=get(handles.H3,'Value');

if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

%LO_pos_fail
blockname=[mname '/Sensors/Measured ',char(10),...
'Left Outer Actuator ',char(10),...
'positions/LO_pos_fail'];
val=get(handles.LO_pos_fail,'Value');

if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

%LI_pos_fail
blockname=[mname '/Sensors/Measured ',char(10),...
'Left Inner Actuator ',char(10),...
'positions/LI_pos_fail'];
val=get(handles.LI_pos_fail,'Value');

if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

%RI_pos_fail

blockname=[mname '/Sensors/Measured ',char(10),...
'Right Inner Actuator ',char(10),...
'positions/RI_pos_fail'];
val=get(handles.RI_pos_fail,'Value');

if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

%RO_pos_fail
blockname=[mname '/Sensors/Measured ',char(10),...
'Right Outer Actuator ',char(10),...
'positions/RO_pos_fail'];
val=get(handles.RO_pos_fail,'Value');
 
if val
    set_param(blockname,'value','1');
else
    set_param(blockname,'value','0');
end

% --- Executes during object creation, after setting all properties.
function figure1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

