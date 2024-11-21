# DS4420_ML-DM2_CourseProject
This is the repository for the CS4420 Machine Learning and Data Mining 2 Course Project at Northeastern University.

- Data
    - For Sentiment Analysis
        - sentiment_dataset

            This is the dataset contains text grabbed from reddit

        - sentiment_result

            This is the rankings we get after sentiment analysis.
        
        - grab_reddit.py

            This is the code using API to grab posts from reddit

            
    - For Feature Engeering
        - amenities_raw_data
            - PDF data for New York

        - feature_dataset
            - FURMAN, FURMANE_csv

                These are the original data for featrure engeering.

            - year_dataset

                This is the dataset made from FURMAN and organized by each year.
                - year_2023

                    The dataset with Walk Score,Bike Score and Transit Score

            - NYC_data.csv dataset_joined.csv

                Final and pre-final version for the feature


        - generate_dataset.ipynb

            This is the code which is used to convert FURMAN into dataset.

- Sentiment Analysis
    - sentiment_analysis.ipynb

        This is the code to do the sentiment analysis for the sentiment_dataset. Here are tools we used in this file.

        1. Libraries
            - VaderSentiment
            - TextBlob
            - AFINN

