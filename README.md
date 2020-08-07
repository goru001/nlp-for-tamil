# NLP for Tamil

This repository contains State of the Art Language models and Classifier
 for Tamil language, which is spoken in India, Srilanka, Malaysia and Singapore.

The models trained here have been used in [Natural Language Toolkit for Indic Languages
 (iNLTK)](https://github.com/goru001/inltk)

## Dataset

#### Created as part of this project
1. [Tamil Wikipedia Articles](https://www.kaggle.com/disisbig/tamil-wikipedia-articles)

2. [Tamil News Dataset](https://www.kaggle.com/disisbig/tamil-news-dataset)

#### Open Source Datasets
1. [iNLTK Headlines Corpus - Tamil](https://github.com/ai4bharat-indicnlp/indicnlp_corpus#publicly-available-classification-datasets) : Uses Tamil News Dataset prepared above.

## Results

### Language Model Perplexity (on validation set)

| Architecture/Dataset | Tamil Wikipedia Articles | Vocab size |
|:--------:|:----:|:----:|
|   ULMFiT  |  19.80  |  8k  |
|  TransformerXL |  18.91  |  8k  |
|  TransformerXL |  17.22  |  16k  |


### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Tamil |  95.22  |  92.70  | [Link](https://github.com/goru001/nlp-for-tamil/blob/master/classification/Tamil_Classifier.ipynb) |
 

### Visualizations
 
##### Word Embeddings

| Architecture | Vocab Size | Visualization |
|:--------:|:----:|:----:|
| ULMFiT | 8k | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-tamil/master/language-model/embedding_projector_config.json) |
| TransformerXL | 8k | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-tamil/master/language-model/embedding_projector_transformer_8k_config.json)  |
| TransformerXL | 16k | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-tamil/master/language-model/embedding_projector_transformer_config.json)  |



### Results of using Transfer Learning + Data Augmentation from iNLTK

##### On using complete training set (with Transfer learning)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Tamil | (5346, 669, 669) | 95.22  |  92.70 | [Link](https://github.com/goru001/nlp-for-tamil/blob/master/classification/Tamil_Classifier.ipynb) |
 

##### On using 5% of training set (with Transfer learning)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Tamil | (267, 669, 669) | 86.25 | 79.42 | [Link](https://github.com/goru001/nlp-for-tamil/blob/master/classification/Tamil_Classifier_without_aug.ipynb) |
 
##### On using 5% of training set (with Transfer learning + Data Augmentation)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Tamil | (267, 669, 669) | 89.84 | 84.63 | [Link](https://github.com/goru001/nlp-for-tamil/blob/master/classification/Tamil_Classifier_with_aug.ipynb) |


## Pretrained Models

#### Language Models 
Download pretrained ULMFiT LM with 8k vocab from [here](https://www.dropbox.com/s/zozzrgawulkwtxa/wikitalm_8k_447_third.pth?dl=0)

Download pretrained TransformerXL LM with 8k vocab from [here](https://drive.google.com/open?id=1ibz5C0Gnz10OadbAZxUVwSDNzHfMq_2O)

Download pretrained TransformerXL LM with 16k vocab from [here](https://drive.google.com/open?id=18LbzazqRrDCYp6sk98kOdWTTMQJvbk0V)

#### Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1JWxkGGrlf4irIuZpOkoXm9EQ8whR1PCA)