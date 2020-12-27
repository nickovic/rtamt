#ifndef STL_COMBINATORIAL_BINARY_NODE_H
#define STL_COMBINATORIAL_BINARY_NODE_H

#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlCombinatorialBinaryNode {
    protected:
        StlOperatorType type;

    public:
        StlCombinatorialBinaryNode(StlOperatorType type);
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_COMBINATORIAL_BINARY_NODE_H */

