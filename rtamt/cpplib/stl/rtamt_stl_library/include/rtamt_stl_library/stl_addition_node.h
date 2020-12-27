#ifndef STL_ADDITION_NODE_H
#define STL_ADDITION_NODE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlAdditionNode : public StlNode {
    public:
        StlAdditionNode();
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_ADDITION_NODE_H */

