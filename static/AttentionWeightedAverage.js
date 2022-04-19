//import * as tf from '@tensorflow/tfjs'
import { InputSpec } from '@tensorflow/tfjs-layers'

 class AttentionWeightedAverage extends tf.layers.Layer {
   constructor(return_attention, config) {
    super(config || {});
     this.supportsMasking = true;
     this.return_attention = return_attention || false;
     this.init = tf.initializers.randomUniform;
   }


   compute_output_shape(inputShape) {
    /*output_len = input_shape[2]
    if self.return_attention:
        return [(input_shape[0], output_len), (input_shape[0],
                                               input_shape[1])]
    return (input_shape[0], output_len)
    return [inputShape[0], inputShape[1], inputShape[2], 2 * inputShape[3]]
    */
    if (this.return_attention == true) {
      return [[inputShape[0], inputShape[2]], [inputShape[0], inputShape[1]]]
    }
    return [inputShape[0], inputShape[2]]
   }

   
   get_output_shape_for(inputShape) {
    return this.compute_output_shape(inputShape);
   }

   
   compute_mask(input, input_mask=None) {
     if (input_mask != None) {
       return [None] * input_mask.length;
     }
     return None;
   }


   build(inputShape) {
    //this.inputSpec = [tf.keras.layers.inputSpec(ndim=3)];
    this.inputSpec = [new InputSpec({ ndim: 4 })];
    console.log(this.name+'_W');
    console.log([inputShape[2], 1]);
    console.log(true);
    console.log(this.init);
    console.log(inputShape.length==3);
    this.W = this.addWeight({name: this.name+'_W',
                             shape: [inputShape[2], 1],
                             trainable: true,
                             initalizer: this.init});
    //super(AttentionWeightedAverage).build(input_shape);
   }
 

   call(x, mask=None) {
    // computes a probability distribution over the timsteps
    // uses 'max trick' for numerical stability
    // reshape is done to avoid issue with Tensorflow and 1-dimensional weights
    logits = tf.backend.dot(x, this.W);
    x_shape = tf.backend.shape(x);
    logits = tf.backend.reshape(logits, (x_shape[0], x_shape[1]));
    ai = tf.backend.exp(lofits - tf.backend.max(logits, axis=-1, keepdims=true));

    // masked timesteps have zero weight
    if (mask != None) {
      mask = tf.backend.cast(mark, tf.backend.floatx());
      ai = ai * mask;
    }
    att_weights = ai / (tf.backend.sum(ai, axis=1, keepdims=true) + tf.backend.epsilon());
    weighted_input = x * tf.backend.expand_dims(att_weights);
    result = tf.backend.sum(weighted_input, axis=1);
    if (this.return_attention == true) {
      return [result, att_weights];
    }
    return result;
   }
 

   static get className() {
     return 'AttentionWeightedAverage';
   }
 }
 tf.serialization.registerClass(AttentionWeightedAverage);  // Needed for serialization.
 
 /*export function attentionWeightedAverage() {
   return new AttentionWeightedAverage();
 }*/
 
/*

class AttentionWeightedAverage(Layer):
    """
    Computes a weighted average of the different channels across timesteps.
    Uses 1 parameter pr. channel to compute the attention value for
    a single timestep.
    """

    def __init__(self, return_attention=False, **kwargs):
        self.init = initializers.get('uniform')
        self.supports_masking = True
        self.return_attention = return_attention
        super(AttentionWeightedAverage, self).__init__(** kwargs)

    def build(self, input_shape):
        self.input_spec = [InputSpec(ndim=3)]
        assert len(input_shape) == 3

        self.W = self.add_weight(shape=(input_shape[2], 1),
                                 name='{}_W'.format(self.name),
                                 trainable=True,
                                 initializer=self.init)
        super(AttentionWeightedAverage, self).build(input_shape)

    def call(self, x, mask=None):
        # computes a probability distribution over the timesteps
        # uses 'max trick' for numerical stability
        # reshape is done to avoid issue with Tensorflow
        # and 1-dimensional weights
        logits = K.dot(x, self.W)
        x_shape = K.shape(x)
        logits = K.reshape(logits, (x_shape[0], x_shape[1]))
        ai = K.exp(logits - K.max(logits, axis=-1, keepdims=True))

        # masked timesteps have zero weight
        if mask is not None:
            mask = K.cast(mask, K.floatx())
            ai = ai * mask
        att_weights = ai / (K.sum(ai, axis=1, keepdims=True) + K.epsilon())
        weighted_input = x * K.expand_dims(att_weights)
        result = K.sum(weighted_input, axis=1)
        if self.return_attention:
            return [result, att_weights]
        return result

    def get_output_shape_for(self, input_shape):
        return self.compute_output_shape(input_shape)

    def compute_output_shape(self, input_shape):
        output_len = input_shape[2]
        if self.return_attention:
            return [(input_shape[0], output_len), (input_shape[0],
                                                   input_shape[1])]
        return (input_shape[0], output_len)

    def compute_mask(self, input, input_mask=None):
        if isinstance(input_mask, list):
            return [None] * len(input_mask)
        else:
            return None


*/