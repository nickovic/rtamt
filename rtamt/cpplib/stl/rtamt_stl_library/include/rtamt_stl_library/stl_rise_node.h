#ifndef STL_RISE_H
#define STL_RISE_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlRiseNode : public StlNode {
    private:
        double prev_in;

    public:
        StlRiseNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_RISE_H */

