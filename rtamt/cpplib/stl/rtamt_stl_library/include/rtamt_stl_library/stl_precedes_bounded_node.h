#ifndef STL_PRECEDES_BOUNDED_NODE_H
#define STL_PRECEDES_BOUNDED_NODE_H

#include <boost/circular_buffer.hpp>

namespace stl_library {

class StlPrecedesBoundedNode {
    private:
        int begin;
        int end;
        boost::circular_buffer<double> buffer[2];
        
    public:
        StlPrecedesBoundedNode(int begin, int end);
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_PRECEDES_BOUNDED_NODE_H */

