#include <rtamt_stl_library/stl_fall_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlFallNode::StlFallNode() {
    prev_in = std::numeric_limits<double>::infinity();
}

void StlFallNode::reset() {
    prev_in = std::numeric_limits<double>::infinity();
}
double StlFallNode::update(double sample) {
    double out = std::min(-sample, prev_in);
    prev_in = sample;
    
    return out;
}

