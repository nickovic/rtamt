#include <rtamt_stl_library/stl_once_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlOnceNode::StlOnceNode() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlOnceNode::reset() {
    prev_out = - std::numeric_limits<double>::infinity();
}

double StlOnceNode::update(double sample) {
    double out;

    out = std::max(sample, prev_out);
    prev_out = out;
    
    return out;
}