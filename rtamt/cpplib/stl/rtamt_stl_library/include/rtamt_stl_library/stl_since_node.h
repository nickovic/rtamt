#ifndef STL_SINCE_NODE_H
#define STL_SINCE_NODE_H

#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlSinceNode : public StlNode {
    private:
        double prev_out;

    public:
        StlSinceNode();
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_SINCE_NODE_H */

