# Resume-Information-Extraction
Corporate firms and enlisting agencies process varied profiles daily. This is often no task for humans. An automatic
intelligent system is needed which may put off all the very important info from the unstructured profile and rework all
of them to a standard structured format. To realize additional attention from the recruiters, most profiles are written in
various formats, together with varied font size, font color, and table cells. However, the variety of format is harmful
to data processing, like profile data extraction, automatic job matching, and candidates ranking. This work proposes
a three step approach for information extraction from profile by, 
      
      [1] Text block identification,
      [2] Vectorization of data, 
      [3] Multi-class classifier to predict different segments of a profile. 
      
Bernoulli Naive Bayes Classifier is used as classification algorithm for prediction.
# Block Identification
In Block Identification step, it segments the resume into different sections on basis of headings and its contents.
The headings can be identified by different font size with respect to the content or by keyword based extraction.
Synonyms of the keyword are also considered in case of keyword based extraction. 

The python code implements Block Identification of the headings which are considered to be
capitalized. Font size of different sections or keyword based on requirement extraction techniques
can also be used for block identification. Resumes can be structured in different formats. One such
format is being extracted for this work. The techniques described above deals with extraction of
different heading strctures. The content extraction function remains the same for every apporach.
The e-mails and phone numbers are also extracted using regular expression.

Prototype for block identification based on capitalized headings is given below. The python code for
the same is attached with the document.

      for each lines in documents do
            for each words in lines do
                  if words matches with keywords or words font size greater than content font size then
                        list the heading words
                  end if
            end for
      end for
      for each word in heading words list do
            function call for content extraction corresponding to each heading
      end for
      Function definition
      for each word in head do
            get the index of word
            get the word correponding to next index from the heading list
            extract the contents between two words as content for first word.
      end for
