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
    prev_out.seq = 0;
    prev_out.time.sec = 0;
    prev_out.time.msec = 0;
    prev_out.value = std::numeric_limits<double>::infinity();
}

void StlAlwaysNode::reset() {
    prev_out.seq = 0;
    prev_out.time.sec = 0;
    prev_out.time.msec = 0;
    prev_out.value = std::numeric_limits<double>::infinity();
}

void StlAlwaysNode::addNewInput(int i, Sample sample) {
    if (i != 0)
        return;
    
    in.seq = sample.seq;
    in.time.sec = sample.time.sec;
    in.time.msec = sample.time.msec;
    in.value = sample.value;
}

void StlAlwaysNode::addNewInput(Sample sample) {
    addNewInput(0,sample);
}

Sample StlAlwaysNode::update() {
    Sample out;
    
    out.seq = in.seq;
    out.time.msec = in.time.msec;
    out.time.sec = in.time.sec;
    out.value = in.value;
    
    out.value = std::min(in.value, prev_out.value);
    
    prev_out.seq = out.seq;
    prev_out.time.sec = out.time.sec;
    prev_out.time.msec = out.time.msec;
    prev_out.value = out.value;
    
    return out;
}

