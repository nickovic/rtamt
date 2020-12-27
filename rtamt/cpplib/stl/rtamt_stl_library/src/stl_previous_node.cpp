#include <rtamt_stl_library/stl_previous_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlPreviousNode::StlPreviousNode() {
    prev_in = std::numeric_limits<double>::infinity();
}

void StlPreviousNode::reset() {
    prev_in = std::numeric_limits<double>::infinity();
}

double StlPreviousNode::update(double sample) {
    double out;
    out = prev_in;
    prev_in = sample;
    
    return out;
}

