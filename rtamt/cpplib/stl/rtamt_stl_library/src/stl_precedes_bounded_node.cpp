/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_precedes_bounded_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlPrecedesBoundedNode::StlPrecedesBoundedNode(int begin, int end) {
    this->begin = begin;
    this->end = end;
    this->buffer[0] = boost::circular_buffer<Sample>(end+1);
    this->buffer[1] = boost::circular_buffer<Sample>(end+1);
    
    int i;
    for(i=0; i <= end; i++) {
        Sample s_left;
        Sample s_right;
        s_left.value = std::numeric_limits<double>::infinity();
        s_right.value = - std::numeric_limits<double>::infinity();
        this->buffer[0].push_back(s_left);
        this->buffer[1].push_back(s_right);
    }
}

void StlPrecedesBoundedNode::reset() {
    int i;
    for(i=0; i <= end; i++) {
        Sample s_left;
        Sample s_right;
        s_left.value = std::numeric_limits<double>::infinity();
        s_right.value = - std::numeric_limits<double>::infinity();
        this->buffer[0].push_back(s_left);
        this->buffer[1].push_back(s_right);
    }
}

void StlPrecedesBoundedNode::addNewInput(int i, Sample sample) {
    if (i < 0 || i > 1)
        return;
    
    in.seq = sample.seq;
    in.time.sec = sample.time.sec;
    in.time.msec = sample.time.msec;
    in.value = sample.value;
    
    this->buffer[i].push_back(in);
}

void StlPrecedesBoundedNode::addNewInput(Sample left, Sample right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

Sample StlPrecedesBoundedNode::update() {
    Sample out;
    
    out.value = - std::numeric_limits<double>::infinity();
    int i;
    for (i=begin; i <= end; i++) {
        Sample left; 
        Sample right;
        right.value = buffer[1][i].value;
        left.value = std::numeric_limits<double>::infinity();
        int j;
        for(j=0; j < i; j++) {
            left.value = std::min(left.value, buffer[0][j].value);
        }
        out.value = std::max(out.value, std::min(left.value, right.value));
    }
    return out;
}