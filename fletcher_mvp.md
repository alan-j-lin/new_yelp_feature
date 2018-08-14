## Project Fletcher MVP

### Domain

For Project Fletcher the domain I am tackling will be bars, I have domain knowledge in that I have opinions on bars.

### Business Problem  

The business problem that I plan on tackling for Project Fletcher is building an alcoholic bar recommender. The user would input a chosen bar and the recommendation engine would build a list of recommended bars based on the profile of the input. The profiles that each bar could be sorted into would be generated using an unsupervised learning method like clustering, while a supervised approach may be utilized in the end to do the actual classification.

### Data:

A majority of the data was downloaded from the yelp challenge [dataset]. Inside is data from 10 different metropolitan areas and contains information regarding the local business, the reviews associated with that business, and the users that reviewed them. In filtering the dataset for only bars that have more than 50 reviews, I end up with about 6000 different businesses which would total to roughly 300k - 400k reviews to analyze. If I need more data I plan on utilizing either the Yelp or TripAdvisor API.

Some features that I believe would be relevant from the reviews data are:  

|   Feature            | Variable Type |
| :---------:          | :-----------: |
| Review Text          | String        |
| Review Rating        | Integer       |

I would in turn be doing feature generation by utilizing the review text for topic modeling or sentiment analysis.

For the business data there are a lot of categorical variables that could possibly be utilized like:  

|   Feature            | Variable Type |
| :---------:          | :-----------: |
| Restaurants Attire   | String        |
| Noise Level          | String        |
| Hours Open           | Integer       |
| Price Range          | Integer       |
| Number of Stars      | Integer       |
| Review Count         | Integer       |
| Has TV               | Boolean       |

One feature I will not be utilizing is ambience, as some businesses have that labeled. That feature may be used in the end to determine to make sense of the clustering.

[dataset]: https://www.yelp.com/dataset/challenge

### Known Unknowns:

A list of some currently known unknowns:  
* 6000 businesses may not be enough especially if spread through 10 metropolitan areas, need to find distribution of selected bars in each area. Would need to interact with Yelp and TripAdvisor APIs if more data is needed.
* Have not identified number of clusters (yelp has 9 for ambience) or classification method.
* For the end product deliverable I would like to build an interface where the user can load a new bar into the interface and get a custom recommendation, time needed for the flask app may be too much.
