#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_not_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_not_node)
{
    class_<StlNotNode, bases<StlNode> >("StlNotNode")
        .def("update", &StlNotNode::update)
        .def("reset", &StlNotNode::reset)
        .def("addNewInput", static_cast<void (StlNotNode::*)(Sample)>(&StlNotNode::addNewInput))
    ;
}

