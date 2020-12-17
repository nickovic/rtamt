/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_always_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlAlwaysNode::StlAlwaysNode() {
    prev_out = std::numeric_limits<double>::infinity();
}

void StlAlwaysNode::reset() {
    prev_out = std::numeric_limits<double>::infinity();
}

void StlAlwaysNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
    in = sample;
}

void StlAlwaysNode::addNewInput(double sample) {
    addNewInput(0, sample);
}

double StlAlwaysNode::update() {
    double out;
    out = std::min(in, prev_out);
    prev_out = out;
    
    return out;
}

