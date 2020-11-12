#ifndef STL_PREVIOUS_H
#define STL_PREVIOUS_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlPreviousNode : public StlNode {
    private:
        Sample in;
        Sample prev_in;
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlPreviousNode();
        Sample update();
        void addNewInput(Sample msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_PREVIOUS_H */

