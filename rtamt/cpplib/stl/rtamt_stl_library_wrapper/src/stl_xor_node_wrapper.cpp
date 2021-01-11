#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_xor_node.h>
#include <rtamt_stl_library/stl_combinatorial_binary_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_xor_node)
{
    class_<StlXorNode, bases<StlCombinatorialBinaryNode> >("XorOperation")
        .def("update", static_cast<double (StlXorNode::*)(double, double)>(&StlXorNode::update))
        .def("reset", &StlXorNode::reset)
    ;
}