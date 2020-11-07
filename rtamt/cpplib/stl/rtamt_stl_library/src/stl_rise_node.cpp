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
    prev_in.seq = 0;
    prev_in.time.sec = 0;
    prev_in.time.msec = 0;
    prev_in.value = - std::numeric_limits<double>::infinity();
}

void StlRiseNode::reset() {
    prev_in.seq = 0;
    prev_in.time.sec = 0;
    prev_in.time.msec = 0;
    prev_in.value = - std::numeric_limits<double>::infinity();
}

void StlRiseNode::addNewInput(int i, Sample sample) {
    if (i != 0)
        return;
    
    in.seq = sample.seq;
    in.time.sec = sample.time.sec;
    in.time.msec = sample.time.msec;
    in.value = sample.value;
}

void StlRiseNode::addNewInput(Sample sample) {
    addNewInput(0,sample);
}

Sample StlRiseNode::update() {
    Sample out;
    
    out.seq = in.seq;
    out.time.msec = in.time.msec;
    out.time.sec = in.time.sec;
    out.value = in.value;
    
    out.value = std::min(in.value, - prev_in.value);
    
    prev_in.seq = in.seq;
    prev_in.time.sec = in.time.sec;
    prev_in.time.msec = in.time.msec;
    prev_in.value = in.value;
    
    return out;
}

