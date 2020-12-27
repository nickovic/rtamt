#ifndef STL_ONCE_BOUNDED_NODE_H
#define STL_ONCE_BOUNDED_NODE_H

#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlOnceBoundedNode {
    private:
        int begin;
        int end;
        boost::circular_buffer<double> buffer;

    public:
        StlOnceBoundedNode(int begin, int end);
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_ONCE_BOUNDED_NODE_H */

