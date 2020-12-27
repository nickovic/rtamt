#ifndef STL_ABS_NODE_H
#define STL_ABS_NODE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlAbsNode : public StlNode {
    public:
        StlAbsNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ABS_NODE_H */

