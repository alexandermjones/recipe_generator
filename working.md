# Get tensorflow js working

## Modify textgenrnn

Change `save` method to be `save` not `save_weights`.
Add to AttentionWeightedAverage:
```
    def get_config(self):

        config = super().get_config().copy()
        config.update({
            'init': self.init,
            'supports_masking': self.supports_masking,
            'self.return_attention': self.return_attention
        })
        return config
```
This follows from: https://stackoverflow.com/questions/58678836/notimplementederror-layers-with-arguments-in-init-must-override-get-conf

## OR Save the model using Keras and the config

```
breakfast_model.model.config = breakfast_model.config
tf.keras.models.save_model(breakfast_model.model, 'breakfast.h5')
```

## Convert the model using tensorflowjs

See here: https://www.tensorflow.org/js/tutorials/conversion/import_saved_model

## Modify the model.json

Want `"class_name": "Model"` rather than `Functional` it's saved as.
Answer here: https://stackoverflow.com/questions/63143849/tensorflow-js-error-unknown-layer-functional

## Define custom Layer for AttentionWeightAverage

Follow final answer: https://stackoverflow.com/questions/50878885/unknown-layer-lambda-in-tensorflowjs-on-browser

Example custom layer: https://github.com/tensorflow/tfjs-examples/blob/master/custom-layer/custom_layer.js
Alternative example: https://github.com/tensorflow/tfjs-examples/blob/master/date-conversion-attention/model.js#L25

