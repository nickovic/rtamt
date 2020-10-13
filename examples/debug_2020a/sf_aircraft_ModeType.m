classdef sf_aircraft_ModeType < Simulink.IntEnumType
    
    %   Copyright 2009-2013 The MathWorks, Inc.
    
    enumeration
        Isolated(0)
        Off(1)
        Passive(2)
        Standby(3)
        Active(4)             
    end
    
    methods (Static)
        
        function defaultValue = getDefaultValue()
            % GETDEFAULTVALUE  Returns the default enumerated value.
            %   If this method is not defined, the first enumeration is used.
            defaultValue = sf_aircraft_ModeType.Isolated;
        end
        
        function dScope = getDataScope()
            % GETDATASCOPE  Specifies whether the data type definition should be imported from,
            %               or exported to, a header file during code generation.
            dScope = 'Auto';
        end
        
        function desc = getDescription()
            % GETDESCRIPTION  Returns a description of the enumeration.
            desc = 'enumeration to track active child state of each L1 state.';
        end
        
        function fileName = getHeaderFile()
            % GETHEADERFILE  Returns path to header file if non-empty.
            fileName = 'sf_aircraft_ModeType.h';
        end
        
        function flag = addClassNameToEnumNames()
            % ADDCLASSNAMETOENUMNAMES  Indicate whether code generator applies the class name as a prefix
            %                          to the enumeration.
            flag = false;
        end
        
    end
    
end
