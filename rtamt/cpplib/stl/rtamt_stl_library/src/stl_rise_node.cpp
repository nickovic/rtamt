#include <rtamt_stl_library/stl_rise_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlRiseNode::StlRiseNode() {
    prev_in = - std::numeric_limits<double>::infinity();
}

void StlRiseNode::reset() {
    prev_in = - std::numeric_limits<double>::infinity();
}

double StlRiseNode::update(double sample) {
    double out;
    
    out = std::min(sample, - prev_in);
    prev_in = sample;
    
    return out;
}

