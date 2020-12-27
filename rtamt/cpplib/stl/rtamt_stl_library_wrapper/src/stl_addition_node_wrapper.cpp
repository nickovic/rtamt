#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_addition_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_addition_node)
{
    class_<StlAdditionNode>("AdditionOperation")
        .def("update", static_cast<double (StlAdditionNode::*)(double, double)>(&StlAdditionNode::update))
        .def("reset", &StlAdditionNode::reset)
    ;
}