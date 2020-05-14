from shapely.geometry import LineString, Polygon

wayPoints = LineString([(-0.3,   0.2),
                        ( 0.0,   0.0),
                        ( 0.4,  -0.2),
                        ( 0.7,  -0.3),
                        ( 0.9,  -0.6)])

prohibitArea1 = Polygon([( 0.5, -0.4),
                         ( 0.8, -0.6),
                         ( 0.8, -0.9),
                         ( 0.5, -0.9)])

prohibitArea2 = Polygon([( -0.5, 0.5),
                         ( -0.8, 0.6),
                         ( -0.8, 0.9),
                         ( -0.5, 0.9),
                         ( -0.3, 0.6)])
                         
egoTargetSpeed = 0.08 #[m/s] Max0.25 [m/s] actually the limit is 0.125
agentTargetSpeed = 0.02 #[m/s]
endTime = 35.0 #[sec]