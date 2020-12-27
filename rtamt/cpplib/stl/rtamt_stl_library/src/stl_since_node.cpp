#include <rtamt_stl_library/stl_since_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlSinceNode::StlSinceNode() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlSinceNode::reset() {
    prev_out = - std::numeric_limits<double>::infinity();
}

double StlSinceNode::update(double left, double right) {
    double out;
    
    out = std::min(left, prev_out);
    out = std::max(out, right);
    
    prev_out = out;
    
    return out;
}