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

void StlCombinatorialBinaryNode::addNewInput(int i, double sample) {
    if (i > 1 or i < 0)
        return;
    
    in[i] = sample;
}

void StlCombinatorialBinaryNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlCombinatorialBinaryNode::update() {
    double val;
    
    switch(type) {
        case AND:
            val = std::min(in[0], in[1]);
            break;
        case OR:
            val = std::max(in[0], in[1]);
            break;
        case IMPLIES:
            val = std::max(-in[0], in[1]);
            break;
        case IFF:
            val = -std::abs(in[0] - in[1]);
            break;
        case XOR:
            val = std::abs(in[0] - in[1]);
            break;
        default:
            val = nan("");
    }

    return val;
}

