#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_constant_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_constant_node)
{
    class_<StlConstantNode, bases<StlNode> >("ConstantOperation", init<double>())
        .def("update", &StlConstantNode::update)
        .def("reset", &StlConstantNode::reset);
}

