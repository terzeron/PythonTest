#!/usr/bin/env python

# https://9bow.github.io/PyTorch-tutorials-kr-0.3.1/beginner/blitz/autograd_tutorial.html

import torch
from torch.autograd import Variable

x = Variable(torch.ones(2, 2), requires_grad=True)
print("x=", x)

y = x + 2
print("y=x+2=", y)
print(y.grad_fn)

z = y * y * 3
print("z=", z)
out = z.mean()
print("out=z.mean()=", out)

# backprop
out.backward()
print("x.grad=", x.grad)

x = torch.randn(3)
y = Variable(x, requires_grad=True)
print("x=", x)
print("y=", y)
y = x * 2
print("y=x*2=", y)
while y.data.norm() < 1000:
    y = y * 2
print(y)

#gradients = torch.FloatTensor([0.1, 1.0, 0.0001])
#print("gradients=", gradients)
#y.backward(gradients)
#print("x.grad=", x.grad)

