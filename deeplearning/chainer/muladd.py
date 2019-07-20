from chainer import Function


class MulAdd(Function):

    def forward_cpu(self, inputs):
        #unpack the input tuple
        x, y, z = inputs
        #computes the output
        w = x*y+z
        #returns a tuple of single element
        return w, #packs it into a tuple

    def backward_cpu(self, inputs, grad_outputs):
        x, y, z = inputs
        grad_w, = grad_outputs
        grad_x = y*grad_w
        grad_y = x*grad_w
        grad_z = grad_w
        return grad_x, grad_y, grad_z
