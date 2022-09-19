#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:56:20 2019

@author: quert
"""

#import tensorflow as tf
#flags = tf.flags # flags is a document, use as processing parametes analysis from terminal 
#FLAGS = flags.FLAGS # FLAGS is an object, store the parameters after analysis
#
## First one is name of parameters, second one is default value, last one is comment
#flags.DEFINE_string("input_file", None, "The dir of input file.")
#flags.DEFINE_string("output_file", None, "The dir of output file")
#flags.DEFINE_integer("batch_size", 256, "The size of a mini-batch")
#
#def main(_): 
#    print("The input file: " + FLAGS.input_file)
#    print("The output file: " + FLAGS.output_file)
#    print("The batch size: " + FLAGS.batch_size)
#    
## Need to add flags.mark_flag_as_required("FLAGS_name")    
#if __name__ == "__main__":
#    flags.mark_flag_as_required("input_file")
#    flags.mark_flag_as_required("output_file")
#    flags.mark_flag_as_required("batch_size")
#    tf.app.run()
#    
    
## Second ptc
import tensorflow as tf

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("input_file", None, "Path of input_file")
flags.DEFINE_string("output_file", None, "Path of output_file")
flags.DEFINE_boolean("bool_value", False, "test_bool")

def main(_):
    print(FLAGS.input_file)
    print(FLAGS.output_file)
    print(FLAGS.bool_value)

if __name__ == '__main__':
    flags.mark_flag_as_required("input_file")
    flags.mark_flag_as_required("output_file")
    flags.mark_flag_as_required("bool_value")
    tf.app.run()