#include <boost/python.hpp>
#include <boost/python/enum.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>

#include <rtamt_stl_library/stl_comp_op.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(stl_comp_op)
{
    enum_<StlComparisonOperator>("StlComparisonOperator")
        .value("LESS", LESS)
        .value("LEQ", LEQ)
        .value("EQUAL", EQUAL)
        .value("NEQ", NEQ)
        .value("GREATER", GREATER)
        .value("GEQ", GEQ)
        ;
}
