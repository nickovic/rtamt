#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_previous_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_previous_node)
{
    class_<StlPreviousNode>("PreviousOperation")
        .def("update", static_cast<double (StlPreviousNode::*)(double)>(&StlPreviousNode::update))
        .def("reset", &StlPreviousNode::reset)
    ;
}

