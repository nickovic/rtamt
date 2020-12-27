#ifndef STL_NODE_H
#define STL_NODE_H

#include <rtamt_stl_library/stl_sample.h>

namespace stl_library {

class StlNode {
    public:
        ~StlNode() {}
        virtual void reset()=0;
};

} // namespace stl_library


#endif /* STL_NODE_H */

