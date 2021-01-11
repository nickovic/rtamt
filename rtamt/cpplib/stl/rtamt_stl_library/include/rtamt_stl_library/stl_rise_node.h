#ifndef STL_RISE_H
#define STL_RISE_H

namespace stl_library {

class StlRiseNode {
    private:
        double prev_in;

    public:
        StlRiseNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_RISE_H */

