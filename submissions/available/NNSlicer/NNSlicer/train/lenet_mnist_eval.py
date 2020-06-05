#  Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Convolutional Neural Network Estimator for MNIST, built with tf.layers."""

from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf

from dataset.config import MNIST_PATH
from dataset import mnist
from model import LeNet
from nninst_utils.fs import abspath

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

# Configs
label = "augmentation"
root_dir = "result/lenet/"

def model_fn(features, labels, mode, params):
    """The model_fn argument for creating an Estimator."""
    model = LeNet(params["data_format"])
    image = features
    if isinstance(image, dict):
        image = features["image"]

    if mode == tf.estimator.ModeKeys.EVAL:
        logits = model(image, training=False)
        loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)
        return tf.estimator.EstimatorSpec(
            mode=tf.estimator.ModeKeys.EVAL,
            loss=loss,
            eval_metric_ops={
                "accuracy": tf.metrics.accuracy(
                    labels=labels, predictions=tf.argmax(logits, axis=1)
                )
            },
        )


def eval(batch_size: int = 64, data_format: str = "channels_first", label: str = None):
    # tf.logging.set_verbosity(tf.logging.INFO)
    if label is None:
        model_dir = abspath(f"{root_dir}/model")
    else:
        model_dir = abspath(f"{root_dir}/model_{label}")
    ckpt_dir = os.path.join(model_dir, "ckpts")
    data_dir = abspath(MNIST_PATH)

    model_function = model_fn

    if data_format is None:
        data_format = (
            "channels_first" if tf.test.is_built_with_cuda() else "channels_last"
        )
    session_config = tf.ConfigProto(allow_soft_placement=True)
    session_config.gpu_options.allow_growth = True
    estimator_config = tf.estimator.RunConfig(session_config=session_config)
    classifier = tf.estimator.Estimator(
        model_fn=model_function,
        model_dir=ckpt_dir,
        params={"data_format": data_format, "batch_size": batch_size},
        config=estimator_config,
    )

    # Evaluate the model and print results
    def eval_input_fn():
        return (
            mnist.test(data_dir).batch(batch_size).make_one_shot_iterator().get_next()
        )

    eval_results = classifier.evaluate(input_fn=eval_input_fn)
    print(label)
    print("Evaluation results:\n\t%s" % eval_results)
    print()


if __name__ == "__main__":
    # fire.Fire(train)
    # eval(label="import")
    eval(label=f"{label}")
