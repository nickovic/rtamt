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
#include <rtamt_stl_library/stl_division_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_division_node)
{
    class_<StlDivisionNode, bases<StlNode> >("StlDivisionNode")
        .def("update", &StlDivisionNode::update)
        .def("reset", &StlDivisionNode::reset)
        .def("addNewInput", static_cast<void (StlDivisionNode::*)(Sample, Sample)>(&StlDivisionNode::addNewInput))
    ;
}