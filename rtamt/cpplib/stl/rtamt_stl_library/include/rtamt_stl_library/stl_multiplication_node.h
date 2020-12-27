#ifndef STL_MULTIPLICATION_NODE_H
#define STL_MUTIPLICATION_NODE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlMultiplicationNode : public StlNode {
    public:
        StlMultiplicationNode();
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_MULTIPLICATION_NODE_H */

