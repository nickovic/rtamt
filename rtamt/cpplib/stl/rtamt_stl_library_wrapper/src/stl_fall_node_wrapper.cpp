#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_fall_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_fall_node)
{
    class_<StlFallNode>("FallOperation")
        .def("update", static_cast<double (StlFallNode::*)(double)>(&StlFallNode::update))
        .def("reset", &StlFallNode::reset)
    ;
}

