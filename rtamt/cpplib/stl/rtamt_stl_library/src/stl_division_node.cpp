#include <rtamt_stl_library/stl_division_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlDivisionNode::StlDivisionNode() {
}

void StlDivisionNode::reset() {
}

double StlDivisionNode::update(double left, double right) {
    double out;
    out = left / right;

    return out;
}

