# house price prediction pipeline
# author: Tejas and Neel Phaterpekar

all: data/processed_train.csv \
data/vectorized_train.csv


# Deal with missing data
data/processed_train.csv: src/process_tweets.py
	python src/process_tweets.py --train_in=data/train.csv --train_out=data/processed_train.csv

# Get document vectors for each text entry
data/vectorized_train.csv: src/vectorize_text.py
	python src/vectorize_text.py --train_in=data/processed_train.csv --train_out=data/vectorized_train.csv

# Remove all files
clean:
	rm -rf data/processed_train.csv
	rm -rf data/vectorized_train.csv