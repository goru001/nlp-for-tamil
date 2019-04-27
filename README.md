# NLP for Tamil
State of the Art Tokenizer, Language model and Classifier for Tamil language (spoken in India, Sri Lanka, Malaysia, Singapore)

## Notebooks
The details below show you how the language model was constructed.

If you want to explore the results, you can checkout the
 [Exploration notebook](https://github.com/goru001/nlp-for-tamil/blob/master/Explore_Pretrained_Tamil_Language_Model.ipynb) and
 open it for free on google colab.

### Dataset preparation
Downloads Wikipedia Articles Dump (>127,000 articles) and
 extract documents using WikiDataExtractor module. 

### Tokenizer
Built tokenizer using Google's
 [sentencepiece](https://github.com/google/sentencepiece).
  Tried various vocabulary sizes and found that 8000 words
is optimal in early experiments. English Hindi etc work well with 30K word-parts, but since Tamil has 
even more complex morphology "(he) is about to go" is one word: "pogavirukkiraan".

### Language Model using Fastai AWD-LSTM (amazing code.)
* Perplexity of Language Model: ~20 

Thanks to Jeremy Howard for his great gift of fastdotai (code, training and encouragement).

### Classifier
* Accuracy of classification model: ~97%
* Kappa score of classification model: ~95

## Datasets

#### Wiki text for language modeling

Download Tamil Wikipedia Articles Dataset (120,000+ articles) from
 [here (training set)](https://www.dropbox.com/s/fsl10ukpbpk51g3/tawiki_train.zip?dl=0) and [here (validation set)](https://www.dropbox.com/s/fsl10ukpbpk51g3/tawiki_train.zip?dl=0).

#### Article snippets for classification

Download Tamil News passages Small Dataset
 (6,000+ short snippets on business, cinema and spirituality)
  from [here](https://www.dropbox.com/s/nobuuiot8qnbogo/Tamil_News_Classification_3class.csv?dl=0) 

Thanks to thetamilhindu headline crawler built using news crawler from [vanangamudi](https://github.com/vanangamudi).

## Model Downloads

### Tokenizer model

Download Tamil sentencepiece Tokenizer : model file from [here](https://www.dropbox.com/s/9q1pkf6c7ahs9qm/tamil_spm_8k.model) and vocab file [here](https://www.dropbox.com/s/5u4l67faq46jbvw/tamil_spm_8k.vocab)

### Language model

Download pretrained Language Model from [here](https://www.dropbox.com/s/zozzrgawulkwtxa/wikitalm_8k_447_third.pth?dl=0)

### Classifier model

Download trained classifier from [here](https://www.dropbox.com/s/3tg0yemgtrevga5/final.pth?dl=0)


## Example result from the language model. 
The ULMFit AWD-LSTM is amazing in its fast ability to learn a model.

Here are some wiki article (totally imagined) by the language model. 
These are not facts, but we can see how well the grammar and even topicality and semantics are learned by it. This quality was unthinkable just a year ago. 

The model learns to properly open and close the tags. It creates well formed urls (though nonexistent). It learns to repeat the title.

And in each article it stays on related places and concepts! But it is truly a random walk in its knowledge store, it is more close to what happens in our dreams where we jump forward losing logical connections :)

Through training on larger dataset and large-span modeling, these could be more and more coherent.


<doc id="9204" url="https: / / ta.wikipedia.org / wiki?curid= xxrep 4 3 " title="விக்கிரமசிங்க"> விக்கிரமசிங்க விக்கிரமசிங்க ("vancarare") என்பது இலங்கையின் கிழக்கு மாகாணத்தில் யாழ்ப்பாண மாவட்டத்தில் அம்பாறை மாவட்டத்தில் உள்ள ஒரு கிராமம் ஆகும். இது யாழ்ப்பாண மாவட்டத்தின் தலைநகரை உள்ளடக்கி இருந்தது. இது யாழ்ப்பாண மாவட்டத்தின் வடமத்தியப் பகுதியில் அமைந்துள்ளது. இது 1770 இல் கட்டப்பட்டு, பின்னர் 1844 இல் பிரித்தானியர் ஆட்சிக்குட்பட்டது. இங்கு இந்துக்களும், இந்துக்களும் பெரும்பான்மையாகக் கொண்ட பேரூர், யாழ்ப்பாணம், மாவேலிக்கரசி, யாழ்ப்பாணம் ஆகிய இடங்களில் வாழ்கின்றனர். இலங்கையில் பெரும்பான்மையாக வாழும் அம்பக்கரக்கள், தமிழ் முஸ்லிம்கள், முஸ்லிம்கள், சிங்களவர், தமிழருக்கு ஒரு பிரிவினர் ஏனையோர் ஆவர். ஏனைய தமிழின மக்கள் தொகை 4, 33,000

 <doc id="9204" url="https: / / ta.wikipedia.org / wiki?curid= xxrep 4 1 04" title="மகாகவி"> மகாகவி மகாகவி, (பிறப்பு: பிப்ரவரி 10, 1954) இலங்கை அரசியல்வாதியும், நாடாளுமன்ற உறுப்பினரும் ஆவார். இவர் பேராதனைப் பல்கலைக்கழகத்தின் (united school of indian) தேசிய சபை (ac)யில் (mc) சட்டமன்ற உறுப்பினராக உள்ளார். இலங்கையின் நாடாளுமன்ற உறுப்பினராக இருந்தும், 2004 முதல் 2010 வரை நாடாளுமன்றத்தில் 35 ஆண்டுகள் பிரதிநிதித்துவப் பதவி வகித்தார். 2010 ஆம் ஆண்டில் ஐக்கிய தேசியக் கட்சியில் இணைந்து நாடாளுமன்ற உறுப்பினராகவும், ஐக்கிய மக்கள் சுதந்திரக் கூட்டணியின் உறுப்பினராகவும் தேர்ந்தெடுக்கப்பட்டார். அட்சாவின் மரணத்திற்குப் பின்னர், இவர் நாடாளுமன்றத்தின் அதிபராக தெரிவுசெய்யப்பட்டார். இவர் தற்போது ஐக்கிய மக்கள் சுதந்திரக் கூட்டணியில் 5வது மக்களவை

 <doc id="9204" url="https: / / ta.wikipedia.org / wiki?curid= xxrep 4 1 04" title="சபீதுர்கான் (துடுப்பாட்டக்காரர்)"> சபீதுர் கான் (துடுப்பாட்டக்காரர்) சபீதுர் கான் (இறப்பு: மார்ச் 10, 2016) ஒரு தென்னிந்தியத் திரைப்பட நடிகர். இவர் மூன்று தமிழ் திரைப்படங்களுக்கு பின்னணியிசைகளுக்கான பின்னணி இசையை இயக்கியுள்ளார். இவர் தற்போது தமிழ் பாடகி மற்றும் திரைப்படத் தயாரிப்பாளர். இவர் தற்போது தமிழ் திரைப்படங்களில் நடிக்கத் துவங்கினார். இவர் திரைப்படத் துறையில் சென்னைக்கு வரும் நடிகராக விளங்குகிறார். தற்போது திரைப்பட இயக்குநர் நிர்மலா "அறிமுகம்" திரைப்படத்தில் நடித்துள்ளார். இவர் "சௌந்தரபாணி" என்ற படத்தில் நடித்ததற்காக சிறந்த நடிகைக்கான தேசிய விருது பெற்றார். இவர் பெரியார், "சத்யஜித்குமாரர்" என்னும் படத்தில் நடித்து

 <doc id="9204" url="https: / / ta.wikipedia.org / wiki?curid= 7708" title="திசையிழையங்கள்"> குருதியிழையங்கள் குருதியிழையங்கள் அல்லது குருதியணுக்களின் குருதியணுக்கள் (ecg plasma) அல்லது குருதியணுக் கலங்கள் ("pyrmond periods") என்பவை புரத நோய்களை கட்டுப்படுத்துவதற்கும், குருதிக் கலங்களுக்குள் உள்ள தாக்கங்களை ஏற்படுத்தி, அவற்றை அணுகவும் பயன்படும் உயிரணுக்களைக் கொண்ட உயிரணுக்களைக் குறிக்கும். இவற்றில் முக்கியக் காரணிகள் உயிரணுக்களின் இனப்பெருக்க உறுப்புக்களே ஆகும். இழையங்கள், இழையங்களின் தொழிற்பாடு, இழையம், இழையம், இழையம் என்பன பொதுவாக ஒரு தனியன் தொகுதியாகவோ அல்லது ஒரே தொகுதியாகவோ இருக்கும். உயிரணுக்கள், இழையங்கள், கொம்புகள், தண்டுகள் போன்றன இழையுரு

 <doc id="9204" url="https: / / ta.wikipedia.org / wiki?curid= xxrep 4 4 " title="பால்வீடசர்"> பால்வீடசர் பால்வீடசர் ("marter") என்பது நாற்புறமும், புறப்பரப்பில் உள்ள மனிதரின் மூளையின் அமைப்பைப் கூறுவதுமாகும். இதன் வழியாகச் செல்லும் அளவு, உடலின் இன்னொரு பகுதி, நாற்புறமும், ஒருவருக்கும் இடையே அமைந்த மடக்கையின் உடல்கள், மற்றும் நாண்கள், நாண்கள், கண்கள், நாக்கு, முள் போன்ற சில உறுப்புகள் இணைந்து இருக்கும். இந்த நாக்கு மேல்முனையில் ஓடும். நாக்கு பகுதி வயிற்றில் செம்பு, கழுத்தின் கீழ் பகுதி, இளம், மார்பு, வயிறு, மார்பு உட்பட பாதங்களை பிடித்து விடுகிறது. நாக்கின் வெளிப்புறத்தில் இருக்கும். தாயின் உடலின் அடி
