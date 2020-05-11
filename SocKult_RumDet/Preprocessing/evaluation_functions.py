#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code contains several versions of evaluation functions
"""
import numpy as np
#from model import LSTM_model_veracity
from model_test import LSTM_model_veracity
import os
from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import f1_score, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from keras.utils.np_utils import to_categorical
from branch2treelabels import branch2treelabels
import pickle
from copy import deepcopy

#%%
def evaluation_function_veracity_branchLSTM(params):
        
    """path = "preprocessing/saved_dataRumEval2019"
    x_train = np.load(os.path.join(path, 'train/train_array.npy'))
    y_train = np.load(os.path.join(path, 'train/fold_stance_labels.npy'))

    print (x_train.shape)

#    ids_train = np.load(os.path.join(path, 'train/tweet_ids.npy'))
    x_dev = np.load(os.path.join(path, 'dev/train_array.npy'))
    y_dev = np.load(os.path.join(path, 'dev/fold_stance_labels.npy'))
#    ids_dev = np.load(os.path.join(path, 'dev/tweet_ids.npy'))
    x_test = np.load(os.path.join(path, 'test/train_array.npy'))
#    y_test = np.load(os.path.join(path, 'test/fold_stance_labels.npy'))
    ids_test = np.load(os.path.join(path, 'test/tweet_ids.npy'))
    # join dev and train
    x_dev = pad_sequences(x_dev, maxlen=len(x_train[0]), dtype='float32',
                          padding='post', truncating='post', value=0.)
    y_dev = pad_sequences(y_dev, maxlen=len(y_train[0]), dtype='float32',
                          padding='post', truncating='post', value=0.)
    
    x_train = np.concatenate((x_train, x_dev), axis=0)
    y_train = np.concatenate((y_train, y_dev), axis=0)
    y_train_cat = []
    for i in range(len(y_train)):
        y_train_cat.append(to_categorical(y_train[i], num_classes=4))
    y_train_cat = np.asarray(y_train_cat)
    y_pred, _ = LSTM_model_stance(x_train, y_train_cat,
                                           x_test, params,eval=True )"""


    # Loading training features  
    x_train_embeddings = np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\train\\embeddings_array.npy")
    x_train_metafeatures = np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\train\\feature_array.npy")

    # Loading the veracity of the tweets True = 0, False = 1, Unverified = 2
    y_train =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\train\\labels.npy")
    unverified_train = np.where(y_train == 2)

    # Removing unverified
    x_train_embeddings = np.delete(x_train_embeddings, unverified_train, 0)
    x_train_metafeatures = np.delete(x_train_metafeatures, unverified_train, 0)
    y_train = np.delete(y_train, unverified_train, 0)

    # Loading the dev features (even though we still call it test, might change)
    x_dev_embeddings =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\dev\\embeddings_array.npy")
    x_dev_metafeatures = np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\dev\\feature_array.npy")

    # Loading the veracity the tweets True = 0, False = 1, Unverified = 2
    y_dev =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\dev\\labels.npy")
    unverified_dev = np.where(y_dev == 2)

    # Removing unverified 
    x_dev_embeddings = np.delete(x_dev_embeddings, unverified_dev, 0)
    x_dev_metafeatures = np.delete(x_dev_metafeatures, unverified_dev, 0)
    y_dev = np.delete(y_dev, unverified_dev, 0)


    # Loading the dev features (even though we still call it test, might change)
    x_test_embeddings =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\test\\embeddings_array.npy")
    x_test_metafeatures = np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\test\\feature_array.npy")

    # Loading the veracity of the test set
    y_test =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\test\\labels.npy")
    
    unverified_test = np.where(y_test == 2)

    # Loading the ids of the test set
    ids_test =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\test\\tweet_ids.npy", allow_pickle=True)

    # Removing unverified
    x_test_embeddings = np.delete(x_test_embeddings, unverified_test, 0)
    x_test_metafeatures = np.delete(x_test_metafeatures, unverified_test, 0)
    y_test = np.delete(y_test, unverified_test, 0)
    ids_test = np.delete(ids_test, unverified_test, 0)


    x_train_embeddings = np.concatenate((x_train_embeddings, x_dev_embeddings), axis = 0)
    x_train_metafeatures = np.concatenate((x_train_metafeatures, x_dev_metafeatures), axis = 0)
    y_train = np.concatenate((y_train, y_dev), axis=0)
    y_train = (to_categorical(y_train, num_classes=2))
    #print(y_train)

    """x_test_embeddings = x_dev_embeddings
    x_test_metafeatures = x_dev_metafeatures
    y_test = y_dev
    ids_test =  np.load("C:\\Users\\sysadmin\\Downloads\\HearSay\\SocKult_RumDet\\Preprocessing\\sacred-twitter-data-w-test\\dev\\tweet_ids.npy", allow_pickle=True)"""

    zero_class = np.where(y_train==0)
    indices = np.random.choice(zero_class[0], 500, replace=False)
    x_train_embeddings = np.delete(x_train_embeddings, indices, 0)
    x_train_metafeatures = np.delete(x_train_metafeatures, indices, 0)
    y_train = np.delete(y_train, indices, 0)

    # Getting predictions and confidence of the model
    y_pred, confidence = LSTM_model_veracity(x_train_embeddings, x_train_metafeatures, y_train,
                                           x_test_embeddings, x_test_metafeatures, params)
    
    #Getting the predictions of trees and the branches
    trees, tree_prediction, tree_label, tree_confidence = branch2treelabels(ids_test, 
                                                              y_test,
                                                              y_pred,
                                                              confidence)
    
    mactest_F = f1_score(tree_label, tree_prediction, average='macro')
        
    return trees, tree_prediction, tree_confidence, mactest_F


# %%
