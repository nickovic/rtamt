#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_implies_node.h>
#include <rtamt_stl_library/stl_combinatorial_binary_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_implies_node)
{
    class_<StlImpliesNode, bases<StlCombinatorialBinaryNode> >("ImpliesOperation")
        .def("update", static_cast<double (StlImpliesNode::*)(double, double)>(&StlImpliesNode::update))
        .def("reset", &StlImpliesNode::reset)
    ;
}