#ifndef STL_CONSTANT_H
#define STL_CONSTANT_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlConstantNode : public StlNode {
    private:
        double val;

    public:
        StlConstantNode(double val);
        double update();
        void reset();
};

} // namespace stl_library

#endif /* STL_NOT_H */

