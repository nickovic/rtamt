/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_precedes_bounded_node.h
 * Author: nickovic
 *
 * Created on August 5, 2019, 10:01 PM
 */

#ifndef STL_PRECEDES_BOUNDED_NODE_H
#define STL_PRECEDES_BOUNDED_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>


namespace stl_library {

class StlPrecedesBoundedNode : public StlNode {
    private:
        int begin;
        int end;
        Sample in;
        boost::circular_buffer<Sample> buffer[2];
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlPrecedesBoundedNode(int begin, int end);
        Sample update();
        void addNewInput(Sample left, Sample right);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_PRECEDES_BOUNDED_NODE_H */

