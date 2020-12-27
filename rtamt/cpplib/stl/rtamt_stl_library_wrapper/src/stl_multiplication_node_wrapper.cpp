#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_multiplication_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_multiplication_node)
{
    class_<StlMultiplicationNode>("MultiplicationOperation")
        .def("update", static_cast<double (StlMultiplicationNode::*)(double, double)>(&StlMultiplicationNode::update))
        .def("reset", &StlMultiplicationNode::reset)
    ;
}