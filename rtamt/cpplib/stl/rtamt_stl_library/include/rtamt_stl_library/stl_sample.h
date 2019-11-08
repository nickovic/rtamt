/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_sample.h
 * Author: nickovic
 *
 * Created on July 31, 2019, 2:56 AM
 */

#ifndef STL_SAMPLE_H
#define STL_SAMPLE_H

namespace stl_library {

struct Time {
    int sec;
    int msec;
};

struct Sample {
    int seq;
    Time time;
    double value;
};


} // namespace stl_library


#endif /* STL_SAMPLE_H */

