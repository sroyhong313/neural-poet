# Neural-Poet

By [Sung Jae Hong](https://github.com/sroyhong313).

## Screenshots
Main Page
![neural-poet_main](/app/static/img/neuralpoet_main.jpg?raw=true "Main Page")
Example Poem
![neural-poet_example](/app/static/img/neuralpoet_sample.jpg?raw=true "Example Poem")
## Description
Neural-Poet is a deep learning agent that has learned to write human-level poetry. It was inspired from Adrej Karpathy's Blog on [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). Having trained old and famous poetry for 40 epochs, it has trained to produce poems of outstanding quality.

## Requirements
Neural-Poet is linked to a mongoDB to store previous poetry that it wrote. The following is required:
* mongoDB 3.4 or higher
* Python 3.x

## Installation
Having a virtualenv setup is recommended. After creating a virtualenv of Python 3.x, run the following:

```python
pip install -r requirements.txt
```
This will instore the dependencies needed to run the Neural-Poet application.
## Usage

After installing all dependencies, run the following to begin mongoDB server:

```console
mongod
```

mongoDB server should now be running in port 27017 (the application assumes it is running on Port 27017).

That is it.
```console
git clone https://github.com/sroyhong313/neural-poet.git
```

```python
python run.py
```

The application should now be on localhost:5000.

## Author

* Sung Jae Hong (https://github.com/sroyhong313)
