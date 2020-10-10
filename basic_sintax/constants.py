# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import tensorflow
tf.__version__


# %%
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# %%
value1 = tf.constant(2)
value2 = tf.constant(3)


# %%
type(value1)


# %%
print(value1)
print(value2)


# %%
soma = value1 + value2
type(soma)


# %%
with tf.Session() as sess:
    s = sess.run(soma)


# %%
print(s)


# %%
text1 = tf.constant('Text 1')
text2 = tf.constant('Text 2')
print(text1)


# %%
with tf.Session() as sess:
    con = sess.run(text1 + text2)


# %%
print(con)


