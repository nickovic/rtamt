#ifndef STL_SUBTRACTION_NODE_H
#define STL_SUBTRACTION_NODE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlSubtractionNode : public StlNode {
    public:
        StlSubtractionNode();
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_SUBTRACTION_NODE_H */

