#ifndef STL_EXP_NODE_H
#define STL_EXP_NODE_H


namespace stl_library {

class StlExpNode {
    public:
        StlExpNode();
        double update(double sample);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_EXP_NODE_H */

