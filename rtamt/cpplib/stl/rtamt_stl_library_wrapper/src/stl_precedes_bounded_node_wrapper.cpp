#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_precedes_bounded_node.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_precedes_bounded_node)
{
    class_<StlPrecedesBoundedNode>("PrecedesBoundedOperation", init<int,int>())
        .def("update", static_cast<double (StlPrecedesBoundedNode::*)(double, double)>(&StlPrecedesBoundedNode::update))
        .def("reset", &StlPrecedesBoundedNode::reset)
    ;
}