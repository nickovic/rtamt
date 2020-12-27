#ifndef STL_HISTORICALLY_NODE_H
#define STL_HISTORICALLY_NODE_H

#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlHistoricallyNode {
    private:
        double prev_out;

    public:
        StlHistoricallyNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_HISTORICALLY_NODE_H */

