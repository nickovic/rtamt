#ifndef STL_IFF_NODE_H
#define STL_IFF_NODE_H

#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlIffNode : public StlCombinatorialBinaryNode {
    public:
        StlIffNode() : StlCombinatorialBinaryNode(IFF) {}      
};

} // namespace stl_library

#endif /* STL_IFF_NODE_H */

