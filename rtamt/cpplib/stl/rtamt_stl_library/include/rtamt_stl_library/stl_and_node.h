#ifndef STL_AND_NODE_H
#define STL_AND_NODE_H

#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_operator_type.h>
namespace stl_library {

class StlAndNode : public StlCombinatorialBinaryNode {
    public:
        StlAndNode() : StlCombinatorialBinaryNode(AND) {}      
};

} // namespace stl_library

#endif /* STL_AND_NODE_H */

