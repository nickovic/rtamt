#ifndef STL_OR_NODE_H
#define STL_OR_NODE_H

#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlOrNode : public StlCombinatorialBinaryNode {
    public:
        StlOrNode() : StlCombinatorialBinaryNode(OR) {}      
};

} // namespace stl_library

#endif /* STL_OR_NODE_H */

