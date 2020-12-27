#ifndef STL_HISTORICALLY_BOUNDED_NODE_H
#define STL_HISTORICALLY_BOUNDED_NODE_H

#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlHistoricallyBoundedNode : public StlNode {
    private:
        int begin;
        int end;
        boost::circular_buffer<double> buffer;

    public:
        StlHistoricallyBoundedNode(int begin, int end);
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_HISTORICALLY_BOUNDED_NODE_H */

