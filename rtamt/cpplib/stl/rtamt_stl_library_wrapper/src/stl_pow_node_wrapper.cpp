#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_pow_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_pow_node)
{
    class_<StlPowNode>("PowOperation")
        .def("update", static_cast<double (StlPowNode::*)(double, double)>(&StlPowNode::update))
        .def("reset", &StlPowNode::reset)
    ;
}

