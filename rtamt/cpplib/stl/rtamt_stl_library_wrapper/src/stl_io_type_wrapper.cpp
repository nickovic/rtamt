#include <boost/python.hpp>
#include <boost/python/enum.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>

#include <rtamt_stl_library/stl_io_type.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(stl_io_type)
{
    enum_<StlIOType>("StlIOType")
        .value("IN", IN)
        .value("OUT", OUT)
        .value("UNKNOWN", UNKNOWN)
        ;
}
