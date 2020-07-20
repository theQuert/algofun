## Scope
- tf.name_scope     
- tf.variable_scope     
```
	with tf.name_scope('name'):
		tf.placeholder(tf.int32, name = "i1")

	with tf.variable_scope('variable'):
		tf.placeholder(tf.int32, name = "i2")
```    

## tf.Variable & tf.get_variable
- tf.Variable     
new 出一個物件, 但同名字的話tf會自行加上node分辨V1, V2
- tf.get_variable     
會檢查撞名問題, 撞名會crash, 但如果撞的是tf.Variable, 會變成V1     
`tf.get_variable`只會在 `variable scope`底下作用
```
	# V 包含 initializer
	with tf.name_scope('name'):
		tf.get_variable(name = "V", shape = [1])

	# variable 包 V 再包 initializer
	with tf.variable_scope('variable'):
		tf.get_variable(name = "V", shape = [1])
```

##### 以tf.get_variable實作網路

## reuse - 宣告 variable 後, 還會再用到 variable
- 用 `variable_scope` 的 `reuse` 取得
```
	with tf.variable_scope('foo'):
		v = tf.get_variable("v", [1])

	assert v1 == v
```