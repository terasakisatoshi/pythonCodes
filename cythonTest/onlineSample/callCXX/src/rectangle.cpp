#include "rectangle.h"
using namespace shapes;

Rectangle::Rectangle(int x_min,int y_min,int x_max,int y_max){
    this->x_min=x_min;
    this->y_min=y_min;
    this->x_max=x_max;
    this->y_max=y_max;
}

Rectangle::~Rectangle(){
    //
}

int Rectangle::getLength(){
    return x_max-x_min;
}

int Rectangle::getHeight(){
    return y_max-y_min;
}

int Rectangle::getArea(){
    return (x_max-x_min)*(y_max-y_min);
}

void Rectangle::move(int dx,int dy){
    x_min+=dx;
    x_max+=dx;

    y_min+=dy;
    y_max+=dy;
}