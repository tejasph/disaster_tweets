# house price prediction pipeline
# author: Tejas and Neel Phaterpekar

all: data/processed_train.csv


# Deal with missing data
data/processed_train.csv: src/process_tweets.py
	python src/process_tweets.py --train_in=data/train.csv --train_out=data/processed_train.csv


# Remove all files
clean:
	rm -rf data/processed_train.csv