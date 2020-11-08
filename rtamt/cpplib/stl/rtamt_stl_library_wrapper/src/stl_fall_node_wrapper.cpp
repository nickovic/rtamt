#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_fall_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_fall_node)
{
    class_<StlFallNode, bases<StlNode> >("StlFallNode")
        .def("update", &StlFallNode::update)
        .def("reset", &StlFallNode::reset)
        .def("addNewInput", static_cast<void (StlFallNode::*)(Sample)>(&StlFallNode::addNewInput))
    ;
}

