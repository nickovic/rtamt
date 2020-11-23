#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_predicate_node.h>
#include <rtamt_stl_library/stl_comp_op.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_predicate_node)
{
    class_<StlPredicateNode, bases<StlNode> >("StlPredicateNode",  init<StlComparisonOperator>())
        .def("update", &StlPredicateNode::update)
        .def("reset", &StlPredicateNode::reset)
        .def("addNewInput", static_cast<void (StlPredicateNode::*)(Sample, Sample)>(&StlPredicateNode::addNewInput))
    ;
}

