cmake_minimum_required(VERSION 3.12)
project(rtamt_stl_library)

## Declare a C++ library
add_library(${PROJECT_NAME}
	SHARED
		src/stl_combinatorial_binary_node.cpp
		src/stl_not_node.cpp 
	  	src/stl_once_node.cpp
	  	src/stl_historically_node.cpp
		src/stl_since_node.cpp
		src/stl_once_bounded_node.cpp
		src/stl_historically_bounded_node.cpp
		src/stl_since_bounded_node.cpp
		src/stl_precedes_bounded_node.cpp
		src/stl_always_node.cpp
		src/stl_eventually_node.cpp
		src/stl_predicate_node.cpp
        src/stl_addition_node.cpp
        src/stl_subtraction_node.cpp
        src/stl_multiplication_node.cpp
        src/stl_division_node.cpp
        src/stl_abs_node.cpp
        src/stl_rise_node.cpp
        src/stl_fall_node.cpp
        src/stl_constant_node.cpp
        src/stl_previous_node.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC ${PROJECT_SOURCE_DIR}/include
)
