#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>

#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_time)
{
    class_<Time>("Time")
        .def_readwrite("sec", &Time::sec)
        .def_readwrite("msec", &Time::msec)
        ;
}
