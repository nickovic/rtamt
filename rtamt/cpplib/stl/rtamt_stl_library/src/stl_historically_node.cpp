/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_historically_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlHistoricallyNode::StlHistoricallyNode() {
    prev_out = std::numeric_limits<double>::infinity();
}

void StlHistoricallyNode::reset() {
    prev_out = std::numeric_limits<double>::infinity();
}

void StlHistoricallyNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
    in = sample;
}

void StlHistoricallyNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlHistoricallyNode::update() {
    double out;
    
    out = std::min(in, prev_out);

    prev_out = out;
    
    return out;
}