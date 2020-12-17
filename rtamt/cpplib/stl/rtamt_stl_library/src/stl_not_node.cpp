/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_not_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlNotNode::StlNotNode() {
}

void StlNotNode::reset() {
}

void StlNotNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
    in = sample;
}

void StlNotNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlNotNode::update() {
    double out;
    out = -in;
    
    return out;
}

