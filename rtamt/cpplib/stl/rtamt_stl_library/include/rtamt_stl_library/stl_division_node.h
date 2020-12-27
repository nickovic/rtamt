#ifndef STL_DIVISION_NODE_H
#define STL_DIVISION_NODE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlDivisionNode : public StlNode {
    private:

    public:
        StlDivisionNode();
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_DIVISION_NODE_H */

