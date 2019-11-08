cmake_minimum_required(VERSION 2.8.3)
project(rtamt_stl_library_wrapper)

find_package(Boost REQUIRED COMPONENTS system python)
find_package(PythonLibs 2.7 REQUIRED)

## Declare a C++ library
add_library(stl_io_type MODULE src/stl_io_type_wrapper.cpp)
add_library(stl_comp_op MODULE src/stl_comp_op_wrapper.cpp)
add_library(stl_node MODULE src/stl_node_wrapper.cpp)
add_library(stl_always_node MODULE src/stl_always_node_wrapper.cpp)
add_library(stl_predicate_node MODULE src/stl_predicate_node_wrapper.cpp)
add_library(stl_time MODULE src/stl_time_wrapper.cpp)
add_library(stl_sample MODULE src/stl_sample_wrapper.cpp)
add_library(stl_not_node MODULE src/stl_not_node_wrapper.cpp)
add_library(stl_operator_type MODULE src/stl_operator_type_wrapper.cpp)
add_library(stl_combinatorial_binary_node MODULE src/stl_combinatorial_binary_node_wrapper.cpp)
add_library(stl_or_node MODULE src/stl_or_node_wrapper.cpp)
add_library(stl_and_node MODULE src/stl_and_node_wrapper.cpp)
add_library(stl_implies_node MODULE src/stl_implies_node_wrapper.cpp)
add_library(stl_iff_node MODULE src/stl_iff_node_wrapper.cpp)
add_library(stl_xor_node MODULE src/stl_xor_node_wrapper.cpp)
add_library(stl_once_node MODULE src/stl_once_node_wrapper.cpp)
add_library(stl_historically_node MODULE src/stl_historically_node_wrapper.cpp)
add_library(stl_since_node MODULE src/stl_since_node_wrapper.cpp)
add_library(stl_once_bounded_node MODULE src/stl_once_bounded_node_wrapper.cpp)
add_library(stl_historically_bounded_node MODULE src/stl_historically_bounded_node_wrapper.cpp)
add_library(stl_since_bounded_node MODULE src/stl_since_bounded_node_wrapper.cpp)
add_library(stl_precedes_bounded_node MODULE src/stl_precedes_bounded_node_wrapper.cpp)


set(INCLUDE_DIRECTORIES_FOR_STL_WRAPPER ${PROJECT_SOURCE_DIR}/include ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
target_include_directories(stl_io_type PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_comp_op PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_always_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_predicate_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_time PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_sample PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_not_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_operator_type PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_combinatorial_binary_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_or_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_and_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_implies_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_iff_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_xor_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_once_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_historically_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_since_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_once_bounded_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_historically_bounded_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_since_bounded_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})
target_include_directories(stl_precedes_bounded_node PUBLIC ${INCLUDE_DIRECTORIES_FOR_STL_WRAPPER})


set(LINK_LIBS_FOR_STL_WRAPPER rtamt_stl_library ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
target_link_libraries(stl_io_type ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_comp_op ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_always_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_predicate_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_time ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_sample ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_not_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_operator_type ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_combinatorial_binary_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_or_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_and_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_implies_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_iff_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_xor_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_once_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_historically_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_since_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_once_bounded_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_historically_bounded_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_since_bounded_node ${LINK_LIBS_FOR_STL_WRAPPER})
target_link_libraries(stl_precedes_bounded_node ${LINK_LIBS_FOR_STL_WRAPPER})


set(LIB_OUT_DIR_FOR_STL_WRAPPER ${RTAMAT_CPPLIB_DIR}/${PROJECT_NAME})
set_target_properties(stl_io_type PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_comp_op PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_always_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_predicate_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_time PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_sample PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_not_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_operator_type PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_combinatorial_binary_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_or_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_and_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_implies_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_iff_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_xor_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_once_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_historically_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_since_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_once_bounded_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_historically_bounded_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_since_bounded_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})
set_target_properties(stl_precedes_bounded_node PROPERTIES
	PREFIX ""
	LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR_FOR_STL_WRAPPER})

# copy __init__.py
configure_file(${PROJECT_SOURCE_DIR}/__init__.py ${LIB_OUT_DIR_FOR_STL_WRAPPER}/__init__.py COPYONLY)
