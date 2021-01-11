#ifndef STL_PREDICATE_NODE_H
#define STL_PREDICATE_NODE_H

#include <rtamt_stl_library/stl_comp_op.h>

namespace stl_library {

class StlPredicateNode {
    private:
        StlComparisonOperator op;

    public:
        StlPredicateNode(StlComparisonOperator op);
        double update(double left, double right);
        void reset();
};

} // namespace stl_library

#endif /* STL_PREDICATE_NODE_H */

