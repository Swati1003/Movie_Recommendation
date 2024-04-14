1) Objective:

To build a movie recommendation system based on genres and keywords. The code takes a user- entered movie title and recommends similar movies using techniques from Machine Learning. The code for movie recommendation system is written in Python Coding Language on Google Collaboratory Platform. 
A movie dataset with columns for titles, genres, and keywords is provided in an Excel spreadsheet. This data is imported into Python as a CSV file.


2) AI Techniques: TF - IDF and Cosine Similarities:

•	The Term Frequence – Inverse Document Frequence (TF – IDF) is a numerical statistic that reflects the importance of a word in a document relative to the entire collection of documents. It considers both the frequency of a word appearing in a specific document (term frequency) and its rarity across all documents (Inverse Document Frequence). Words that are frequent in a specific document but rare overall get a higher TF – IDF score, indicating their relevance. 

For example, 
Movie A is an Action Movie, and has key words such as “Guns, Crime, Fight.” The TF – IDF score for these words are high but are less common across all movies. Movie B is a Comedy Movie, and has key words such as “Funny” and “Laughter,” which have high TF – IDF score but are more common. By focusing on most relevant keywords and genres, TF – IDF help recommend movies that share similar themes and styles.

•	Cosine Similarity is a metric used to measure the similarity between two documents (or vectors) by calculating the cosine of the angle between them. Documents with similar word usage will have high cosine similarity scores, indicating they share similar content. 

In this case, it is applied between the feature vector of the user – entered movie and all the other movies in the dataset. Movies with higher cosine similarity score share more keywords and likely belong to similar genres, leading to recommendations of similar movies.
