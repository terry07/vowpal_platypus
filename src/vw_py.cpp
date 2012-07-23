#include "vw_py.h"

#include <iostream>
#include <vowpalwabbit/vw.h>
#include <vowpalwabbit/example.h>
#include <cassert>

vw _vw;
bool _initialized = false;

void initialize(char* params) {
    cout << "initialized with params=[" << std::string(params) << "]" << endl;
    _vw = VW::initialize(std::string(params));
    _initialized = true;
}

void finalize() {
    assert(_initialized);
    VW::finish(_vw);
}

float learn(char* line) {
    assert(_initialized);

    cout << "no1" << "[" << line << "]" << endl;
    example* v = VW::read_example(_vw, line);

    cout << "no3" << endl;
    _vw.learn(&_vw, v);
    float p = v->final_prediction;
    cout << "no5" << endl;
    VW::finish_example(_vw, v);
    cout << "no6" << "[" << p << "]" << endl;
    return p;
}
