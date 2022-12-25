# Pytorch: reshape(), view()
### The id of variable
```Python3
a = torch.arange(12)
b = a.reshape(3, 4)
b[:] = 12
print(a) # a is same as b
```
By applying `reshape`, the variable would not be copied. It uses the original address to store the changed values.

### What is reshape() capable of?

### What is reshape() can do, but view() cannot do?
