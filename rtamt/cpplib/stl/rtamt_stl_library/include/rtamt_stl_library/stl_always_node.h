/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_always_node.h
 * Author: nickovic
 *
 * Created on July 8, 2019, 3:27 PM
 */

#ifndef STL_ALWAYS_NODE_H
#define STL_ALWAYS_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlAlwaysNode : public StlNode {
    private:
        Sample in;
        Sample prev_out;
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlAlwaysNode();
        Sample update();
        void addNewInput(Sample msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ALWAYS_NODE_H */

