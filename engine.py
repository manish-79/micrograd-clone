#first lets create a class that can store values and other data related to them

class Value:
  def __init__(self,data,label="",_op="",_children=()):
    self.data = data
    self.label = label
    self._op = _op
    self._prev = _children

  def __repr__(self):
    return f"Value(data: {self.data})"

  def __add__(self,other):
    print("started add function")
    other = other if isinstance(other,Value) else Value(other)
    print(f"add self: {self}, other:{other}")
    out = Value(self.data + other.data, _op="+", _children=(self,other))
    return out

  def __mul__(self,other):
    other = other if isinstance(other,Value) else Value(other)
    out = Value(self.data * other.data, _op="*", _children=(self,other))
    return out

  def __pow__(self,other):
    assert isinstance(other,(int,float))
    out = Value(self.data ** other,_op=f"**{other}",_children=(self,))
    return out

  def __truediv__(self,other):
    return self * other**(-1)

  def __rtruediv(self,other):
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
