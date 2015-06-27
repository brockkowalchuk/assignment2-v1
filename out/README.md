# assignment2-v1
1. Input necessary credentials to access TWTR data
2. Connected to AWS with unique user identifiers
3. For ease of use, preloaded multiple queries to be analyzed in TWTR (q1, q2, and q3)
4. Wrote function, pullTweets
 Looked at past 7 days from 06-18 to 06-25
    Please note I had significant issues here! 
 Converted tweets to utf-8 and avoided excess information
 Due to lack of tweets, I chunked my data in groups of 20 with a unique file name that would be a multiple of 20. 
 I printed out the number of tweets for easy reference

 The frequency distribution was analyzed using nltk
 First I needed to tokenize my text file
    This only worked after converting the text file to utf-8
 Secondly, I plotted this distribution (left max y-axis at 400)
  
