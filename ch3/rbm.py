from tensorflow.keras import layers
import tensorflow_probability as tfp

class RBM(layers.Layer):
    def __init__(self,number_hidden_units=10,number_visible_units=None,learning_rate=0.1,cd_steps=1):
        super().__init__()
        self.number_hidden_units=number_hidden_units,
        self.number_visible_units=number_visible_units
        self.learning_rate=learning_rate
        self.cd_steps=cd_steps

    def build(self,input_shape):
        pass

    def forward(self,x):
        pass

    def sample_h(self,x):
        pass

    def reverse(self,x):
        pass

    def sample_v(self,x):
        pass

    def call(self,inputs):
        pass

    def free_energy(self,x):
        pass

    def reverse_gibbs(self,x):
        pass

    def cd_update(self,x):
        pass

    def reconstruction_cost(self,x):
        pass
    