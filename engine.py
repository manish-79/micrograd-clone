import math
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

class Value:
  def __init__(self,data,label="",_op="",_children=()):
    self.data = data
    self.label = label
    self.grad = 0.0
    self._op = _op
    self._prev = _children
    self._backward = lambda : None

  def __repr__(self):
    return f"Value(data: {self.data})"

  def __add__(self,other):
    other = other if isinstance(other,Value) else Value(other)
    out = Value(self.data + other.data, _op="+", _children=(self,other))
    def _backward():
      self.grad += 1.0 * out.grad
      other.grad += 1.0 * out.grad
    out._backward = _backward
    return out

  def __mul__(self,other):
    other = other if isinstance(other,Value) else Value(other)
    out = Value(self.data * other.data, _op="*", _children=(self,other))
    def _backward():
      self.grad += other.data * out.grad
      other.grad += self.data * out.grad
    out._backward = _backward
    return out

  def __pow__(self,other):
    assert isinstance(other,(int,float))
    out = Value(self.data ** other,_op=f"**{other}",_children=(self,))
    def _backward():
      self.grad += (other * (self.data **(other-1))) * out.grad
    out._backward = _backward
    return out

  def __truediv__(self,other):
    return self * other**(-1)

  def __rtruediv__(self,other):
    return other * self**(-1)

  def __radd__(self,other):
    return self + other

  def __rmul__(self,other):
    return self * other

  def __neg__(self):
    return -1*self

  def __sub__(self,other):
    return self + (-other)

  def __rsub__(self,other):
    return other + (-self)

  def tanh(self):
    x = self.data
    t = (math.exp(2*x)-1)/(math.exp(2*x)+1)
    out = Value(t,_op="tanh",_children=(self,))
    def _backward():
      self.grad += (1-t**2)*out.grad
    out._backward = _backward
    return out

  def backward(self):
    topo = []
    visited = set()

    def buildtopo(v):
        if v not in visited:
            visited.add(v)
            for child in v._prev:
                buildtopo(child)
            topo.append(v)


    for node in reversed(topo):
      node._backward()
