#ifndef STL_PREVIOUS_H
#define STL_PREVIOUS_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlPreviousNode : public StlNode {
    private:
        double in;
        double prev_in;
        void addNewInput(int i, double msg);
        
        
    public:
        StlPreviousNode();
        double update();
        void addNewInput(double msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_PREVIOUS_H */

