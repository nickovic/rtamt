#ifndef STL_ONCE_NODE_H
#define STL_ONCE_NODE_H

#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlOnceNode : public StlNode {
    private:
        double prev_out;

    public:
        StlOnceNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_ONCE_NODE_H */

