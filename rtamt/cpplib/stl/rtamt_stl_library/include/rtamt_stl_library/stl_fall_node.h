/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_rise.h
 * Author: nickovic
 *
 * Created on August 3, 2019, 5:23 PM
 */

#ifndef STL_FALL_H
#define STL_FALL_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlFallNode : public StlNode {
    private:
        Sample in;
        Sample prev_in;
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlFallNode();
        Sample update();
        void addNewInput(Sample msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_RISE_H */

