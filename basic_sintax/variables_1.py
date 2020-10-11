# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import tensorflow as tf


# %%
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# %%
value1 = tf.constant(15, name="value1")
print(value1)


# %%
sums = tf.Variable(value1 + 5)


# %%
print(sums)
type(sums)


# %%
init = tf.global_variables_initializer()


# %%
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sums))


