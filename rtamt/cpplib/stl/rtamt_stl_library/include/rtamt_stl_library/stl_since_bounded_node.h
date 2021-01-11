#ifndef STL_SINCE_BOUNDED_NODE_H
#define STL_SINCE_BOUNDED_NODE_H

#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlSinceBoundedNode {
    private:
        int begin;
        int end;
        boost::circular_buffer<double> buffer[2];

    public:
        StlSinceBoundedNode(int begin, int end);
        double update(double left, double right);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_SINCE_BOUNDED_NODE_H */

