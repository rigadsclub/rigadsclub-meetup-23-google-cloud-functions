import unittest

import tensorflow as tf


class MyTestCase(unittest.TestCase):
    def test_predict(self):
        model = tf.keras.models.load_model('./model')
        sample = {
            'district': 'Centrs',
            'rooms': 5,
            'floor': 1,
            'total_floors': 2,
            'area': 1,
        }

        input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
        price = model.predict(input_dict)[0][0]
        self.assertEqual(price, 179.32927)


if __name__ == '__main__':
    unittest.main()
