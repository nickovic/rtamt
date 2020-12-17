#include <rtamt_stl_library/stl_subtraction_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlSubtractionNode::StlSubtractionNode() {
}

void StlSubtractionNode::reset() {
}

void StlSubtractionNode::addNewInput(int i, double sample) {
    if (i > 1 or i < 0)
        return;
    
    in[i] = sample;
}

void StlSubtractionNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlSubtractionNode::update() {
    double out;

    out = in[0] - in[1];

    return out;
}

