#include <rtamt_stl_library/stl_multiplication_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlMultiplicationNode::StlMultiplicationNode() {
}

void StlMultiplicationNode::reset() {
}

double StlMultiplicationNode::update(double left, double right) {
    double out;
    out = left * right;
    return out;
}

