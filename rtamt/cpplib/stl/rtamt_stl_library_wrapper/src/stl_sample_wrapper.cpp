#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>

#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_sample)
{
    class_<Sample>("Sample")
        .def_readwrite("seq", &Sample::seq)
        .def_readwrite("time", &Sample::time)
        .def_readwrite("value", &Sample::value)
        ;
}

