#include <rtamt_stl_library/stl_eventually_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlEventuallyNode::StlEventuallyNode() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlEventuallyNode::reset() {
    prev_out = - std::numeric_limits<double>::infinity();
}
double StlEventuallyNode::update(double sample) {
    double out;
    
    out = std::max(sample, prev_out);
    prev_out = out;
    
    return out;
}