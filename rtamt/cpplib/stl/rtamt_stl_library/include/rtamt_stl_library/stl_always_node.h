#ifndef STL_ALWAYS_NODE_H
#define STL_ALWAYS_NODE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlAlwaysNode : public StlNode {
    private:
        double prev_out;

    public:
        StlAlwaysNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ALWAYS_NODE_H */

