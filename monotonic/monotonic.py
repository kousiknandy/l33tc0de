import operator
import functools

monotonic = lambda seq, op: all(op(seq[i], seq[i+1]) for i in range(len(seq)-1))
strictly_increasing = functools.partial(monotonic, op=operator.lt)
non_decreasing = functools.partial(monotonic, op=operator.le)

