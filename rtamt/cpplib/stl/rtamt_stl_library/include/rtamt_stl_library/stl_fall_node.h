#ifndef STL_FALL_H
#define STL_FALL_H

namespace stl_library {

class StlFallNode {
    private:
        double prev_in;

    public:
        StlFallNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_RISE_H */

