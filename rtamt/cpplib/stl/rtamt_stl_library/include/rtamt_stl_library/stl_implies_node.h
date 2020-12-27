#ifndef STL_IMPLIES_NODE_H
#define STL_IMPLIES_NODE_H

#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlImpliesNode : public StlCombinatorialBinaryNode {
    public:
        StlImpliesNode() : StlCombinatorialBinaryNode(IMPLIES) {}      
};

} // namespace stl_library

#endif /* STL_IMPLIES_NODE_H */

