/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_since_node.h
 * Author: nickovic
 *
 * Created on August 6, 2019, 8:45 AM
 */

#ifndef STL_SINCE_NODE_H
#define STL_SINCE_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>


namespace stl_library {

class StlSinceNode : public StlNode {
    private:
        double in[2];
        double prev_out;
        void addNewInput(int i, double msg);
        
        
    public:
        StlSinceNode();
        double update();
        void addNewInput(double left, double right);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_SINCE_NODE_H */

