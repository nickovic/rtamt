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
    this->buffer = boost::circular_buffer<double>(end+1);
    
    int i;
    for(i=0; i <= end; i++) {
        double s;
        s = std::numeric_limits<double>::infinity();
        this->buffer.push_back(s);
    }
}

void StlHistoricallyBoundedNode::reset() {

    int i;
    for(i=0; i <= end; i++) {
        double s;
        s = std::numeric_limits<double>::infinity();
        this->buffer.push_back(s);
    }
}

void StlHistoricallyBoundedNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;

    this->buffer.push_back(sample);
}

void StlHistoricallyBoundedNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlHistoricallyBoundedNode::update() {
    double out;
    
    out = std::numeric_limits<double>::infinity();
    int i;
    for (i=0; i <= end - begin; i++) {
        out = std::min(out, buffer[i]);
    }
    return out;
}