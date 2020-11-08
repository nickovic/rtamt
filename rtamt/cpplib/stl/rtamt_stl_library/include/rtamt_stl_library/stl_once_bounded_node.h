/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_once_bounded_node.h
 * Author: nickovic
 *
 * Created on August 5, 2019, 8:12 PM
 */

#ifndef STL_ONCE_BOUNDED_NODE_H
#define STL_ONCE_BOUNDED_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>


namespace stl_library {

class StlOnceBoundedNode : public StlNode {
    private:
        int begin;
        int end;
        Sample in;
        boost::circular_buffer<Sample> buffer;
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlOnceBoundedNode(int begin, int end);
        Sample update();
        void addNewInput(Sample msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ONCE_BOUNDED_NODE_H */

