/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_rise_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlRiseNode::StlRiseNode() {
    prev_in = - std::numeric_limits<double>::infinity();
}

void StlRiseNode::reset() {
    prev_in = - std::numeric_limits<double>::infinity();
}

void StlRiseNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
    in = sample;
}

void StlRiseNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlRiseNode::update() {
    double out;
    
    out = std::min(in, - prev_in);
    prev_in = in;
    
    return out;
}

