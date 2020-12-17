#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_previous_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_previous_node)
{
    class_<StlPreviousNode, bases<StlNode> >("PreviousOperation")
        .def("update", &StlPreviousNode::update)
        .def("reset", &StlPreviousNode::reset)
        .def("addNewInput", static_cast<void (StlPreviousNode::*)(double)>(&StlPreviousNode::addNewInput))
    ;
}

