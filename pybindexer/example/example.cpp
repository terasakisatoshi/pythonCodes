#include<math.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include<stdio.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

void print_some(float img[30*30]){
    for (int i = 0; i < 30; ++i)
    {
        for (int j = 0; j < 30; ++j)
        {
            printf("%d",(int)img[30*i+j]);
        }
        printf("\n");
    }
}

std::vector<float> get_tensor(std::vector<float> image) {
    int width=sqrt(image.size());
    int height=sqrt(image.size());
    std::vector<float> flatten(width * height, 0.0);
    float* fpimage = &image[0];
    print_some(fpimage);
    for (int i = 0; i < height; ++i)
    {
        for (int j = 0; j < width; ++j)
        {
            flatten[i * width + j] = fpimage[i * width + j];
        }
    }
    return flatten;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin";
    m.def("get_tensor", &get_tensor, "get tensor and return flatten as vector");
    m.def("add", &add, "A function which adds two numbers");
}
