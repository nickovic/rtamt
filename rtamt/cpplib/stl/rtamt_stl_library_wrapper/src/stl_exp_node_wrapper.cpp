#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_exp_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_exp_node)
{
    class_<StlExpNode>("ExpOperation")
        .def("update", static_cast<double (StlExpNode::*)(double)>(&StlExpNode::update))
        .def("reset", &StlExpNode::reset)
    ;
}

