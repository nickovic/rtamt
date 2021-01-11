#include <rtamt_stl_library/stl_subtraction_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlSubtractionNode::StlSubtractionNode() {
}

void StlSubtractionNode::reset() {
}

double StlSubtractionNode::update(double left, double right) {
    double out;

    out = left - right;

    return out;
}

