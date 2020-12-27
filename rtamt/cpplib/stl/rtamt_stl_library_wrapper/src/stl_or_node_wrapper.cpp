#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_or_node.h>
#include <rtamt_stl_library/stl_combinatorial_binary_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_or_node)
{
    class_<StlOrNode, bases<StlCombinatorialBinaryNode> >("OrOperation")
        .def("update", static_cast<double (StlOrNode::*)(double, double)>(&StlOrNode::update))
        .def("reset", &StlOrNode::reset)
    ;
}