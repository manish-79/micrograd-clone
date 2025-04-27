import random

class Neuron:
  def __init__(self,nin):
    self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
    self.b = Value(random.uniform(-1,1))

  def __call__(self,inlist):
    act = (sum(w*x for w,x in zip(self.w,inlist))) + self.b
    out = act.tanh()
    return out

class Layer:
  def __init__(self,nin,nout):
    self.neurons = [Neuron(nin) for _ in range(nout)]

  def __call__(self,x):
    outs = [n(x) for n in self.neurons]
    return outs[0] if len(outs)==1 else outs

class MLP:
  def __init__(self,nin,nout):
    s = [nin] + nout
    self.layers = [Layer(s[i],s[i+1])for i in range(len(s)-1)]

  def __call__(self, x):
      for layer in self.layers:
          x = layer(x)
      return x
