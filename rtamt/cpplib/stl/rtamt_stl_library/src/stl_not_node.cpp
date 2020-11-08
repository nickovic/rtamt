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

void StlNotNode::addNewInput(int i, Sample sample) {
    if (i != 0)
        return;
    
    in.seq = sample.seq;
    in.time.sec = sample.time.sec;
    in.time.msec = sample.time.msec;
    in.value = sample.value;
}

void StlNotNode::addNewInput(Sample sample) {
    addNewInput(0,sample);
}

Sample StlNotNode::update() {
    Sample out;
    
    out.seq = in.seq;
    out.time.msec = in.time.msec;
    out.time.sec = in.time.sec;
    out.value = -in.value;
    
    return out;
}

