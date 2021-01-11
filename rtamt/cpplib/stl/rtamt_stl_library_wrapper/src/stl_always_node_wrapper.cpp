#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_always_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_always_node)
{
    class_<StlAlwaysNode>("AlwaysOperation", init<>())
        .def("update", static_cast<double (StlAlwaysNode::*)(double)>(&StlAlwaysNode::update))
        .def("reset", &StlAlwaysNode::reset)
    ;
}

