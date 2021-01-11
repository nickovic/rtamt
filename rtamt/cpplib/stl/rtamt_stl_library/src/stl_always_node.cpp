#include <rtamt_stl_library/stl_always_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlAlwaysNode::StlAlwaysNode() {
    prev_out = std::numeric_limits<double>::infinity();
}

void StlAlwaysNode::reset() {
    prev_out = std::numeric_limits<double>::infinity();
}

double StlAlwaysNode::update(double sample) {
    double out;
    out = std::min(sample, prev_out);
    prev_out = out;
    
    return out;
}

