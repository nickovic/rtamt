/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_since_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlSinceNode::StlSinceNode() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlSinceNode::reset() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlSinceNode::addNewInput(int i, double sample) {
    if (i < 0 || i > 1)
        return;
    
    in[i] = sample;
}

void StlSinceNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlSinceNode::update() {
    double out;
    
    out = std::min(in[0], prev_out);
    out = std::max(out, in[1]);
    
    prev_out = out;
    
    return out;
}