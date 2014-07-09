import theano

theano.config.floatX = 'float32'
x = theano.tensor.scalar()
x.dtype
theano.config.floatX = 'float64'
x = theano.tensor.scalar()
x.dtype
