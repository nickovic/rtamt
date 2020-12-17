#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>

using namespace boost::python;
using namespace stl_library;

struct StlNodeWrap : StlNode, wrapper<StlNode>
{
    double update() {
        return this->get_override("update")();
    }
    
    void addNewInput(int i, double msg) {
        this->get_override("addNewInput")(i, msg);
    }
};


BOOST_PYTHON_MODULE(stl_node)
{
    class_<StlNodeWrap, boost::noncopyable>("Operation")
        .def("update", pure_virtual(&StlNode::update))
    ;
}

