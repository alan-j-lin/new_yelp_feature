# A Bar Recommender

For this project, I tried to implement to a feature in Yelp that I wish existed. When you search a business on Yelp it will give you similar businesses beside the one that you had searched for, however this search only extends to businesses in the area. I can not search for bars that are similar to bar X from SF when I go to another place, for instance Chicago. This businesses profile and recommender is what I decided to then build which would take in up to three bars as inputs to find bars that were similar in a given locale. I decided to subset on bars as the type of bar that a person likes is very particular to them. For this project I ended up using the Yelp challenge [dataset] which has information on business in 12 different metropolitan locations in the US and Canada. The data being spread out over different areas was important as I wanted my recommender to be location agnostic.

[dataset]: https://www.yelp.com/dataset/challenge

**Repository Structure**

* Flask: Flask app that I built utilizing my model. Copy of this will be on a different repo which will be deployed on Heroku
* fletcher_MVP.md: Document describing my minimum viable product for this project.
* BarRecommendation_Project.ipynb: Jupyter notebook containing the code and graphics used to build the model for this project
