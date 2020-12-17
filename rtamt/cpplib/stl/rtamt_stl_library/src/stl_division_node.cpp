#include <rtamt_stl_library/stl_division_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlDivisionNode::StlDivisionNode() {
}

void StlDivisionNode::reset() {
}

void StlDivisionNode::addNewInput(int i, double sample) {
    if (i > 1 or i < 0)
        return;
    in[i] = sample;
}

void StlDivisionNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlDivisionNode::update() {
    double out;
    out = in[0] / in[1];

    return out;
}

