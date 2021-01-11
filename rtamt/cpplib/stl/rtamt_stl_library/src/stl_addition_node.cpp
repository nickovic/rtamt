#include <rtamt_stl_library/stl_addition_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlAdditionNode::StlAdditionNode() {
}

void StlAdditionNode::reset() {
}

double StlAdditionNode::update(double left, double right) {
    double out;

    out = left + right;

    return out;
}

