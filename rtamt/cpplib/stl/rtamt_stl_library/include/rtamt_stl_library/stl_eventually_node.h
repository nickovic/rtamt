#ifndef STL_EVENTUALLY_NODE_H
#define STL_EVENTUALLY_NODE_H

namespace stl_library {

class StlEventuallyNode {
    private:
        double prev_out;

    public:
        StlEventuallyNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_EVENTUALLY_NODE_H */

