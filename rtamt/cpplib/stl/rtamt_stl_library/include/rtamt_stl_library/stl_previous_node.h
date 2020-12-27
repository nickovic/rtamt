#ifndef STL_PREVIOUS_H
#define STL_PREVIOUS_H

#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlPreviousNode : public StlNode {
    private:
        double prev_in;

    public:
        StlPreviousNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_PREVIOUS_H */

