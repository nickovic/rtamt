/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_historically_bounded_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlHistoricallyBoundedNode::StlHistoricallyBoundedNode(int begin, int end) {
    this->begin = begin;
    this->end = end;
    this->buffer = boost::circular_buffer<Sample>(end+1);
    
    int i;
    for(i=0; i <= end; i++) {
        Sample s;
        s.value = std::numeric_limits<double>::infinity();
        this->buffer.push_back(s);
    }
}

void StlHistoricallyBoundedNode::reset() {

    int i;
    for(i=0; i <= end; i++) {
        Sample s;
        s.value = std::numeric_limits<double>::infinity();
        this->buffer.push_back(s);
    }
}

void StlHistoricallyBoundedNode::addNewInput(int i, Sample sample) {
    if (i != 0)
        return;
    
    in.seq = sample.seq;
    in.time.sec = sample.time.sec;
    in.time.msec = sample.time.msec;
    in.value = sample.value;
    
    this->buffer.push_back(in);
}

void StlHistoricallyBoundedNode::addNewInput(Sample sample) {
    addNewInput(0,sample);
}

Sample StlHistoricallyBoundedNode::update() {
    Sample out;
    
    out.value = std::numeric_limits<double>::infinity();
    int i;
    for (i=0; i <= end - begin; i++) {
        out.value = std::min(out.value, buffer[i].value);
    }
    return out;
}