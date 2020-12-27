#ifndef STL_FALL_H
#define STL_FALL_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlFallNode : public StlNode {
    private:
        double prev_in;

    public:
        StlFallNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_RISE_H */

