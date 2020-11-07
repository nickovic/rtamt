/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_operator_type.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_combinatorial_binary_node)
{
    class_<StlCombinatorialBinaryNode, bases<StlNode> >("StlCombinatorialBinaryNode", init<StlOperatorType>())
        .def("update", &StlCombinatorialBinaryNode::update)
        .def("reset", &StlCombinatorialBinaryNode::reset)
        .def("addNewInput", static_cast<void (StlCombinatorialBinaryNode::*)(Sample, Sample)>(&StlCombinatorialBinaryNode::addNewInput))
    ;
}