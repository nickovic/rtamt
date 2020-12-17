#include <rtamt_stl_library/stl_addition_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlAdditionNode::StlAdditionNode() {
}

void StlAdditionNode::reset() {
}

void StlAdditionNode::addNewInput(int i, double sample) {
    if (i > 1 or i < 0)
        return;
    
    in[i] = sample;
}

void StlAdditionNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlAdditionNode::update() {
    double out;

    out = in[0] + in[1];

    return out;
}

