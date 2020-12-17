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

void StlPreviousNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
   in = sample;
}

void StlPreviousNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlPreviousNode::update() {
    double out;
    out = prev_in;
    prev_in = in;
    
    return out;
}

