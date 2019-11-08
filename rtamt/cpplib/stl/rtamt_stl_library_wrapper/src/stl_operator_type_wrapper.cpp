/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <boost/python.hpp>
#include <boost/python/enum.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>

#include <rtamt_stl_library/stl_operator_type.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(stl_operator_type)
{
    enum_<StlOperatorType>("StlOperatorType")
        .value("UNDEFINED", UNDEFINED)
        .value("PREDICATE", PREDICATE)
        .value("NOT", NOT)
        .value("OR", OR)
        .value("AND", AND)
        .value("IMPLIES", IMPLIES)
        .value("IFF", IFF)
        .value("XOR", XOR)
        .value("EV", EV)
        .value("ALWAYS", ALWAYS)
        .value("UNTIL", UNTIL)
        .value("ONCE", ONCE)
        .value("HIST", HIST)
        .value("SINCE", SINCE)
        ;
}