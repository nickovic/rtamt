#ifndef STL_SUBTRACTION_NODE_H
#define STL_SUBTRACTION_NODE_H

namespace stl_library {

class StlSubtractionNode {
    public:
        StlSubtractionNode();
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_SUBTRACTION_NODE_H */

