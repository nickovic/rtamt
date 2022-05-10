#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_sqrt_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_sqrt_node)
{
    class_<StlSqrtNode>("SqrtOperation")
        .def("update", static_cast<double (StlSqrtNode::*)(double)>(&StlSqrtNode::update))
        .def("reset", &StlSqrtNode::reset)
    ;
}

