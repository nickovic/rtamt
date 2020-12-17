#include <rtamt_stl_library/stl_multiplication_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlMultiplicationNode::StlMultiplicationNode() {
}

void StlMultiplicationNode::reset() {
}

void StlMultiplicationNode::addNewInput(int i, double sample) {
    if (i > 1 or i < 0)
        return;
    
    in[i] = sample;
}

void StlMultiplicationNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlMultiplicationNode::update() {
    double out;

    out = in[0] * in[1];
 

    return out;
}

