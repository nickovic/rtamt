/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_fall_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlFallNode::StlFallNode() {
    prev_in = std::numeric_limits<double>::infinity();
}

void StlFallNode::reset() {
    prev_in = std::numeric_limits<double>::infinity();
}

void StlFallNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
    in = sample;
}

void StlFallNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlFallNode::update() {
    double out = std::min(-in, prev_in);
    prev_in = in;
    
    return out;
}

