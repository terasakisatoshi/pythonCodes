#include <iostream>
#include <pybind11/embed.h>
#include <pybind11/pybind11.h>
#include <pyscience11/matplotlib.h>
#include <pyscience11/matplotlib/pyplot.h>
#include <pyscience11/numpy.h>
#include <pyscience11/scipy/special.h>

namespace py = pybind11;
namespace m11 = matplotlib11;
namespace n11 = numpy11;
namespace s11 = scipy11;

int main(void)
{
    // 組み込み Python インタプリタを起動する
    py::scoped_interpreter interpreter;

    // numpy と scipy.special を読み込む
    auto numpy = n11::import_numpy();
    auto scipy_special = s11::scipy::import_special();

    // 誤差関数 (erf) を計算する
    auto x = numpy.linspace(-2, 2, 1001, py::arg("dtype") = numpy.attr("float32"));
    auto y = scipy_special.erf(x);

    // matplotlib を読み込み、バックエンドを設定する
    auto matplotlib = m11::import_matplotlib();
    //matplotlib.use("TkAgg");

    // グラフを描画する
    auto pl = m11::matplotlib::import_pyplot();
    std::cout<<"HELLO"<<std::endl;

    return 0;
}