#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_once_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_once_node)
{
    class_<StlOnceNode>("OnceOperation")
        .def("update", static_cast<double (StlOnceNode::*)(double)>(&StlOnceNode::update))
        .def("reset", &StlOnceNode::reset)
    ;
}