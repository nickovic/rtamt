#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

// Initialize previous and current value
StlCombinatorialBinaryNode::StlCombinatorialBinaryNode(StlOperatorType type) {
    this->type = type;
    
}

void StlCombinatorialBinaryNode::reset() {
}

double StlCombinatorialBinaryNode::update(double left, double right) {
    double val;
    
    switch(type) {
        case AND:
            val = std::min(left, right);
            break;
        case OR:
            val = std::max(left, right);
            break;
        case IMPLIES:
            val = std::max(-left, right);
            break;
        case IFF:
            val = -std::abs(left - right);
            break;
        case XOR:
            val = std::abs(left - right);
            break;
        default:
            val = nan("");
    }

    return val;
}

