#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_always_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_always_node)
{
    class_<StlAlwaysNode, bases<StlNode> >("StlAlwaysNode", init<>())
        .def("update", &StlAlwaysNode::update)
        .def("reset", &StlAlwaysNode::reset)
        .def("addNewInput", static_cast<void (StlAlwaysNode::*)(Sample)>(&StlAlwaysNode::addNewInput))
    ;
}

