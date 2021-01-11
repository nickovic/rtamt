#ifndef STL_XOR_NODE_H
#define STL_XOR_NODE_H

#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlXorNode : public StlCombinatorialBinaryNode {
    public:
        StlXorNode() : StlCombinatorialBinaryNode(XOR) {}      
};

} // namespace stl_library



#endif /* STL_XOR_NODE_H */

