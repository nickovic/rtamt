/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_eventually_node.h
 * Author: nickovic
 *
 * Created on August 6, 2019, 8:50 AM
 */

#ifndef STL_EVENTUALLY_NODE_H
#define STL_EVENTUALLY_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlEventuallyNode : public StlNode {
    private:
        Sample in;
        Sample prev_out;
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlEventuallyNode();
        Sample update();
        void addNewInput(Sample msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_EVENTUALLY_NODE_H */

