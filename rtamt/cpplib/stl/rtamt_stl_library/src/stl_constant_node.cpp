#include <rtamt_stl_library/stl_constant_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlConstantNode::StlConstantNode(double val) {
    this->val = val;
}

void StlConstantNode::reset() {
}

double StlConstantNode::update() {
    return this->val;
}

