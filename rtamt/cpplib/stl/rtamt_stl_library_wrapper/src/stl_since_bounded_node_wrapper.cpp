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
#include <rtamt_stl_library/stl_since_bounded_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_since_bounded_node)
{
    class_<StlSinceBoundedNode, bases<StlNode> >("StlSinceBoundedNode", init<int,int>())
        .def("update", &StlSinceBoundedNode::update)
        .def("reset", &StlSinceBoundedNode::reset)
        .def("addNewInput", static_cast<void (StlSinceBoundedNode::*)(Sample, Sample)>(&StlSinceBoundedNode::addNewInput))
    ;
}