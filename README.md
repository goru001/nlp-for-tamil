# NLP for Tamil

This repository contains State of the Art Language models and Classifier
 for Tamil language, which is spoken in India, Srilanka, Malaysia and Singapore.

The models trained here have been used in [Natural Language Toolkit for Indic Languages
 (iNLTK)](https://github.com/goru001/inltk)

## Dataset

#### Created as part of this project
1. [Tamil Wikipedia Articles](https://www.kaggle.com/disisbig/tamil-wikipedia-articles)

2. [Tamil News Dataset](https://www.kaggle.com/disisbig/tamil-news-dataset)


## Results

#### Language Model Perplexity

| Architecture/Dataset | Tamil Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  19.80  |
|  TransformerXL |  17.22  |


#### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | Kappa Score |
|:--------:|:----:|:----:|
| Tamil News Dataset |  96.78  |  95.09  |


#### Visualizations
 
##### Embedding Space

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection with 8k vocab](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-tamil/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection with 16k vocab](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-tamil/master/language-model/embedding_projector_transformer_config.json)  |
| TransformerXL | [Embeddings projection with 8k vocab](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-tamil/master/language-model/embedding_projector_transformer_8k_config.json)  |


## Pretrained Language Model

Download pretrained ULMFiT LM with 8k vocab from [here](https://www.dropbox.com/s/zozzrgawulkwtxa/wikitalm_8k_447_third.pth?dl=0)

Download pretrained TransformerXL LM with 8k vocab from [here](https://drive.google.com/open?id=1ibz5C0Gnz10OadbAZxUVwSDNzHfMq_2O)

Download pretrained TransformerXL LM with 16k vocab from [here](https://drive.google.com/open?id=18LbzazqRrDCYp6sk98kOdWTTMQJvbk0V)

## Classifier

Download trained classifier from [here](https://drive.google.com/open?id=1fmiXpH7B9ujAR81SscUcx1W1mFw9DZdy)

## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1JWxkGGrlf4irIuZpOkoXm9EQ8whR1PCA)