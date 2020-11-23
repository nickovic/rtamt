#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_abs_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_abs_node)
{
    class_<StlAbsNode, bases<StlNode> >("StlAbsNode")
        .def("update", &StlAbsNode::update)
        .def("addNewInput", static_cast<void (StlAbsNode::*)(Sample)>(&StlAbsNode::addNewInput))
        .def("reset", &StlAbsNode::reset)
    ;
}

