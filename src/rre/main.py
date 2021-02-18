import os
import tensorflow as tf

from google.cloud import storage

model = None

def download_blob(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('riga-ds-club-playground-models')
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def predict():
    sample = {
        'district': 'Centrs',
        'rooms': 5,
        'floor': 1,
        'total_floors': 2,
        'area': 1,
    }

    input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
    return model.predict(input_dict)[0]


def handle(request):
    global model
    if model is None:
        os.makedirs('/tmp/model/variables/')
        download_blob('rre/saved_model.pb',
                      '/tmp/model/saved_model.pb')
        download_blob('rre/variables/variables.data-00000-of-00001',
                      '/tmp/model/variables/variables.data-00000-of-00001')
        download_blob('rre/variables/variables.index',
                      '/tmp/model/variables/variables.index')
        model = tf.keras.models.load_model('/tmp/model')

    return str(predict())
