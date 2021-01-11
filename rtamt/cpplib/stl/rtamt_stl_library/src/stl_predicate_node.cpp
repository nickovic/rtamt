#include <rtamt_stl_library/stl_predicate_node.h>
#include <cmath>

using namespace stl_library;

StlPredicateNode::StlPredicateNode(StlComparisonOperator op) {
    this->op = op;
}

void StlPredicateNode::reset() {
}

double StlPredicateNode::update(double left, double right) {
    double out;
    
    switch(op) {
        case EQUAL:
            out = -std::abs(left - right);
            break;
        case NEQ:
            out = std::abs(left - right);
            break;
        case LEQ:
        case LESS:
            out = right - left;
            break;
        case GEQ:
        case GREATER:
            out = left - right;
            break;
    }
    
    return out;
}
