#!/usr/bin/env python

from __future__ import print_function
import torch

x = torch.empty(5, 3) # uninitialized 5x3 array
print(x)

x = torch.rand(5, 3) # random 5x3 array
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)

# make new tensor from existing tensor
x = x.new_ones(5, 3, dtype=torch.double)
print(x)
x = torch.randn_like(x, dtype=torch.float)
print(x)

print(x.size())
print(x.size()[0], x.size()[1])

# operations
y = torch.rand(5, 3)
print("x=", x)
print("y=", y)
print("x + y =", x + y)

print("add(x, y) =", torch.add(x, y))

y.add_(x)
print("y=", y)

print("x=", x)
print("x[:, 1]=", x[:, 1]) # 1th columns

# transformation
x = torch.randn(4, 4)
print("x=", x)
y = x.view(16)
print("y=x.view(16)=", y) # 1D
z = x.view(-1, 8)
print("z=x.view(-1, 8)=", z) # 2D (2x8), -1 means estimation
print("x.size()=", x.size(), "y.size()=", y.size(), "z.size()=", z.size())

a = torch.ones(5)
print("a=", a)
b = a.numpy() # transform a into numpy array
print("b=", b)
a.add_(1)
print(a)
print(b)






