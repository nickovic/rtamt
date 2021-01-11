#include <rtamt_stl_library/stl_not_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlNotNode::StlNotNode() {
}

void StlNotNode::reset() {
}

double StlNotNode::update(double sample) {
    double out;
    out = -sample;
    
    return out;
}

