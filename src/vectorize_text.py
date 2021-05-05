# vectorize_text.py
# Tejas Phaterpekar
# April 28 2021

'''This script takes in a tweet and processes it

Usage: vectorize_text.py --train_in=<train_in> --train_out=<train_out>


Options: 
--train_in=<train_in>   :   String to be processed
--train_out=<train_out>   : out path

''' 


from docopt import docopt
import pandas as pd
import spacy
import numpy as np

# parse/define command line arguments here
opt = docopt(__doc__)

def main(train_in, train_out):

    # load dataset and spacy model
    train_df = pd.read_csv(train_in)
    nlp = spacy.load("en_core_web_md")

    print("Vectorizing text")
    # create a df containing our document vectors
    train_v = pd.DataFrame(np.vstack([vectorize(entry, nlp) for entry in train_df.text]))
    
    # Stick ids back on
    final_train_df = pd.concat([train_df[['id']], train_v], axis = 1)

    # Output for processed tweets
    final_train_df.to_csv(train_out, index = False)


def vectorize(item, nlp):
    doc = nlp(item)
    return doc.vector


    # call main function
if __name__ == "__main__":
    main(opt["--train_in"], opt['--train_out'])