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
    this->buffer[0] = boost::circular_buffer<double>(end+1);
    this->buffer[1] = boost::circular_buffer<double>(end+1);
    
    int i;
    for(i=0; i <= end; i++) {
        double s_left;
        double s_right;
        s_left = std::numeric_limits<double>::infinity();
        s_right = - std::numeric_limits<double>::infinity();
        this->buffer[0].push_back(s_left);
        this->buffer[1].push_back(s_right);
    }
}

void StlPrecedesBoundedNode::reset() {
    int i;
    for(i=0; i <= end; i++) {
        double s_left;
        double s_right;
        s_left = std::numeric_limits<double>::infinity();
        s_right = - std::numeric_limits<double>::infinity();
        this->buffer[0].push_back(s_left);
        this->buffer[1].push_back(s_right);
    }
}

void StlPrecedesBoundedNode::addNewInput(int i, double sample) {
    if (i < 0 || i > 1)
        return;
    
    in = sample;
    
    this->buffer[i].push_back(in);
}

void StlPrecedesBoundedNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlPrecedesBoundedNode::update() {
    double out;
    
    out = - std::numeric_limits<double>::infinity();
    int i;
    for (i=begin; i <= end; i++) {
        double left; 
        double right;
        right = buffer[1][i];
        left = std::numeric_limits<double>::infinity();
        int j;
        for(j=0; j < i; j++) {
            left = std::min(left, buffer[0][j]);
        }
        out = std::max(out, std::min(left, right));
    }
    return out;
}