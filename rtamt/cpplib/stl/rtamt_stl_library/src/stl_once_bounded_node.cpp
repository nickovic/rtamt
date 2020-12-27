#include <rtamt_stl_library/stl_once_bounded_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlOnceBoundedNode::StlOnceBoundedNode(int begin, int end) {
    this->begin = begin;
    this->end = end;
    this->buffer = boost::circular_buffer<double>(end+1);
    
    int i;
    for(i=0; i <= end; i++) {
        double s;
        s = - std::numeric_limits<double>::infinity();
        this->buffer.push_back(s);
    }
}

void StlOnceBoundedNode::reset() {
    int i;
    for(i=0; i <= end; i++) {
        double s;
        s = - std::numeric_limits<double>::infinity();
        this->buffer.push_back(s);
    }
}

double StlOnceBoundedNode::update(double sample) {
    double out;

    this->buffer.push_back(sample);
    
    out = - std::numeric_limits<double>::infinity();
    int i;
    for (i=0; i <= end - begin; i++) {
        out = std::max(out, buffer[i]);
    }
    return out;
}