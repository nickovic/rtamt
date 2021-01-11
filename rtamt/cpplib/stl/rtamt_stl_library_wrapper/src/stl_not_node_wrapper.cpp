#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_not_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_not_node)
{
    class_<StlNotNode>("NotOperation")
        .def("update", static_cast<double (StlNotNode::*)(double)>(&StlNotNode::update))
        .def("reset", &StlNotNode::reset)
    ;
}

