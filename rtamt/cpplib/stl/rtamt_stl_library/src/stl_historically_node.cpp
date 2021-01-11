#include <rtamt_stl_library/stl_historically_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlHistoricallyNode::StlHistoricallyNode() {
    prev_out = std::numeric_limits<double>::infinity();
}

void StlHistoricallyNode::reset() {
    prev_out = std::numeric_limits<double>::infinity();
}

double StlHistoricallyNode::update(double sample) {
    double out;
    
    out = std::min(sample, prev_out);

    prev_out = out;
    
    return out;
}