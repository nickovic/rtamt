#ifndef STL_PREVIOUS_H
#define STL_PREVIOUS_H

namespace stl_library {

class StlPreviousNode {
    private:
        double prev_in;

    public:
        StlPreviousNode();
        double update(double sample);
        void reset();
};

} // namespace stl_library

#endif /* STL_PREVIOUS_H */

