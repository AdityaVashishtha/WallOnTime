import json
import random


def read_quotes():
    with open('quotes_data.json') as f:
        lines = (l.strip() for l in f)
        return [json.loads(l.decode('utf-8')) for l in lines if l]


def loadQuote():
    quotes = read_quotes()
    authors = list(set(author for _, author in quotes))
    quote, author = random.choice(quotes)        
    quote_line = ''
    count = 0
    char_count = 0
    for w in quote.split():
        count = count + 1
        char_count += len(w)
        quote_line = quote_line+' '+w
        if(count >= 4 or char_count >= 24):
            quote_line += "\n"
            count = 1
            char_count = 1                 
    # quote = (quote.encode('utf-8')),'-',(author.encode('utf-8'))
    # print quote
    author = '- '+author
    return quote_line,author
