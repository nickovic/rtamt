#ifndef STL_CONSTANT_H
#define STL_CONSTANT_H

namespace stl_library {

class StlConstantNode {
    private:
        double val;

    public:
        StlConstantNode(double val);
        double update();
        void reset();
};

} // namespace stl_library

#endif /* STL_NOT_H */

