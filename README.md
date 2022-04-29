# RIS_Final_Version

SECTION1: terms for file names
- N: NLTK
- B: BERT
- Neu: neutral sentiment posts
- dw: data wrangling
- sth + ed: the file after this action e.g., Ned refers to files after NTLK scoring; Neucleaned refers to dataset after neutral be cleaned
- skl: sklearn
- sns: seaborn
- relvscore: relevant scoring
- comp: company related data
- gov: government related data
- iden: which NLTK and BERT agrees in sentiment
- ALL: data generated all 24 months in ONE table
- valley: data from valley sentiment month
- peak: data from peak sentiment month
- FOUR: data including 1) all tweets with NLTK score; 2) all tweets with BERT score; 3) all tweets which NLTK and BERT agrees in sentiment 4) all tweets
- with two scores (one for NLTK one for BERT)
- ** temp_ AND ALL_: all the final version of data visualization should be found in files of these two types of names


SECTION2: names of all coding files 
NOTIFICATION: for data wrangling, each steps contains 24 files named from Jan2018 to Dec2019 (1801 - 1912)
  - T_mined.py // this is the file for mining data from Twitter
    output: csv file with columns = ['author_id', 'created_at', 'id', 'lang', 'text']
    output file name: output_year+month.csv e.g., "out_1801.csv"
  
  - D_clean.py // this is the file for cleaning the unrelated information in twwets e.g. hashtags, URL links with regular expression
    output: stuctured tabular form of data with columns = ['author_id', 'created_at', 'id', 'lang', 'text']
    output file name: dwed_year+month.csv e.g., "dwed_1801.csv"
  
  - NLTK_score.py // this is the file for getting NLTK score of tweets
    output: tabular form of data with original columns + NLTK score
    output file name: Ned_year+month.csv e.g., ""Ned_1801.csv"
  
  - NLTK_noneu.py // this is the file for cleaning rows of tweets with has neutral sentiment outcome
    output: tabular form of data with non-neutral sentment tweets
    output file name: Neucleaned_year+month.csv e.g., 'Neucleaned_1801.csv'
    
  - (file not in this package) // this is the file of BERT model runned in Google Colab
    output: tabular form of data with original columns + BERT score
    output file name: bertout_year+month.csv
  
  - outcome_ana.py // this is the file to combine all 24 months files into one table
    output: an overall giant tabular form of data with all outcomes with column = ['author_id', 'created_at', 'text', 'score','BERTscore']
    output file name: multi files include a) files with tweets with NLTK and BERT have the same sentiment
                                          b) files with tweet with NLTK and BERT have different sentiment
  
  - outcome_ana_combination.py; outcome_ana_temp.py; outcome_ana_v2.py; outcome_ana_v3.py // all contains some ways of sorting data
     output file name: ALL_for_compare.csv || ALL_for_combine.csv, etc...
