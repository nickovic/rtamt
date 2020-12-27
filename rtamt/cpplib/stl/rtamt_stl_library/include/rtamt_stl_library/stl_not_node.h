#ifndef STL_NOT_H
#define STL_NOT_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlNotNode : public StlNode {
    private:

    public:
        StlNotNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_NOT_H */

