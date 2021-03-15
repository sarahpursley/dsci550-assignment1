# AgePredictor

https://github.com/USCDataScience/AgePredictor

## Build and Run
Build then drop into the container
```
docker build . --tag agepredict
docker run -it agepredict /bin/bash
```

## Quickstart
Now, you can run AgePredict normally! Once inside the container, begin Quickstart steps. Note that the working directory is the AgePredict project's root directory.
1. Perform training, and build a ```model/en-ageClassify.bin``` file:
```
bin/authorage AgeClassifyTrainer -model model/en-ageClassify.bin -lang en -data data/sample_train.txt -encoding UTF-8
```

2. Run the Age prediction with the sample data:
```
bin/authorage AgePredict model/classify-unigram.bin model/regression-global.bin data/sample_test.txt
```

3. Run the Age prediction and grep out the predictions from the sample data:
```
bin/authorage AgePredict ./model/classify-unigram.bin ./model/regression-global.bin data/sample_test.txt < data/sample_test.txt 2>&1 | grep "Prediction"
```

## Usage
Place all of your testing/training data in the local ```data/``` directory. For additional usage see the [AgePredictor](https://github.com/USCDataScience/AgePredictor) documentation.

### Example
Coming...
