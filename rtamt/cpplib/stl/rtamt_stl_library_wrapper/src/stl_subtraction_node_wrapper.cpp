#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_subtraction_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_subtraction_node)
{
    class_<StlSubtractionNode>("SubtractionOperation")
        .def("update", static_cast<double (StlSubtractionNode::*)(double, double)>(&StlSubtractionNode::update))
        .def("reset", &StlSubtractionNode::reset)
    ;
}