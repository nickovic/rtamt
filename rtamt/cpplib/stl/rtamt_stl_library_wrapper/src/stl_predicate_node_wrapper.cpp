#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_predicate_node.h>
#include <rtamt_stl_library/stl_comp_op.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_predicate_node)
{
    class_<StlPredicateNode>("PredicateOperation",  init<StlComparisonOperator>())
        .def("update", static_cast<double (StlPredicateNode::*)(double, double)>(&StlPredicateNode::update))
        .def("reset", &StlPredicateNode::reset)
    ;
}

