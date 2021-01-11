#ifndef STL_ALWAYS_NODE_H
#define STL_ALWAYS_NODE_H

namespace stl_library {

class StlAlwaysNode {
    private:
        double prev_out;

    public:
        StlAlwaysNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ALWAYS_NODE_H */

