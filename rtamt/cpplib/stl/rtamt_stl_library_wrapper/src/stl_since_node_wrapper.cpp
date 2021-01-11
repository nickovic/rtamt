#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_since_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_since_node)
{
    class_<StlSinceNode>("SinceOperation")
        .def("update", static_cast<double (StlSinceNode::*)(double, double)>(&StlSinceNode::update))
        .def("reset", &StlSinceNode::reset)
    ;
}