# process_tweets.py
# Tejas Phaterpekar
# April 28 2021

'''This script takes in a tweet and processes it

Usage: process_tweets.py --train_in=<train_in> --train_out=<train_out>


Options: 
--train_in=<train_in>   :   String to be processed
--train_out=<train_out>   : out path

''' 

from docopt import docopt
import re
import pandas as pd

# parse/define command line arguments here
opt = docopt(__doc__)

def main(train_in, train_out):

    df = pd.read_csv(train_in)

    # remove any urls
    df['text'] = df['text'].apply(lambda x: process_tweet(x))

    # remove duplicates
    df = df[df.duplicated(subset = ['text']) != True]

    # Output for processed tweets
    df.to_csv(train_out, index = False)


def process_tweet(tweet):
    '''
    Processes our tweets. Needed because some tweets are showing up as 
    duplicates with slightly different url addresses
    
    tweet -- (String)
    '''
    
    # remove any urls
    updated_tweet = re.sub(r"http\S+"," ", tweet).rstrip()
    
    return updated_tweet

# call main function
if __name__ == "__main__":
    main(opt["--train_in"], opt['--train_out'])