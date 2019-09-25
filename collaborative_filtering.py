from movie_recommendation_data import dataset
from math import sqrt

# print "Lisa Rose rating on Lady in the water: {}\n".format(dataset['Lisa Rose']['Lady in the Water'])
# print "Michael Phillips rating on Lady in the water: {}\n".format(dataset['Michael Phillips']['Lady in the Water'])
#
# print '**************Jack Matthews ratings**************'
# print dataset['Jack Matthews']

def similarity_score(person1,person2):

    # Returns ratio Euclidean distance score of person1 and person2
    both_viewed = {} # to get both rated items by person1 and person2

    for item in dataset[person1]:
        if item in dataset[person2]:
            both_viewed[item]=1

    #Conditions to check they both have a common rating items
    if len(both_viewed)==0:
        return 0

    #Finding euclidean distance =[]

    sum_of_euclidean_distance =[]
    for item in dataset[person1]:
        if item in dataset[person2]:
            sum_of_euclidean_distance.append(pow(dataset[person1][item]-dataset[person2][item],2))
    sum_of_euclidean_distance=sum(sum_of_euclidean_distance)
    return 1/(1+sqrt(sum_of_euclidean_distance))



def pearson_correlation(person1,person2):

    # Returns Pearson Correlation coefficient of person1 and person2
    #To get both rated items
    both_rated = {}
    for item in dataset[person2]:
        if item in dataset[person2]:
            both_rated[item]=1

    number_of_ratings = len(both_rated)

    #Checking for number of ratings in common
    if number_of_ratings == 0:
        return 0

    #Add up all the preferences of each user
    person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])

    # sum of squares of preferences squares of each user
    person1_square_preferences_sum = sum([pow(dataset[person1][item],2)for item in both_rated])
    person2_square_preferences_sum = sum([pow(dataset[person2][item],2)for item in both_rated])

    # sum up the product value of both preferences for each item
    sum_of_product_both_users = sum ([dataset[person1][item]* dataset[person2][item] for item in both_rated])

    #calculate the pearson score

    numerator = sum_of_product_both_users -( person1_preferences_sum * person2_preferences_sum / number_of_ratings)
    denominator = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings)
                       *(person2_square_preferences_sum - pow(person2_preferences_sum,2)/number_of_ratings))

    if denominator==0:
        return 0
    else:
        r = numerator/denominator
        return r

########### Finding the most similar persons to a particular user ###########3

def most_similar_persons(person, number_of_persons):
    # returns the number_of_users (similar persons) for a given specific person.
    scores = [(pearson_correlation(person, other_person), other_person) for other_person in dataset if
          other_person != person]
    # Sort the similar persons so that highest scores person will appear at the first
    scores.sort()
    scores.reverse()
    return scores[0:]

#print most_similar_persons('Lisa Rose', 3)      #### using pearson correlation   measure

# print 'Jack Matthews to Lisa Rose using Least Euclidean Distance Ratio :',similarity_score("Lisa Rose","Jack Matthews")      #### using euclidean distance measure
# print 'Jack Matthews to Lisa Rose using Pearson Correlation :',pearson_correlation("Lisa Rose","Jack Matthews")              #### using pearson correlation   measure
# print 'Jack Matthews to Gene Seymour using Pearson Correlation :',pearson_correlation('Lisa Rose','Gene Seymour')            #### using pearson correlation   measure
#print dataset["Lisa Rose"]
def user_recommendations(person):
    # Gets recommendations for a person by using a weighted average of every other user's ranking
    totals = {}
    simSums = {}
    print dataset
    for other in dataset:
        # don't compare me to myself
        if other == person:
            continue

        sim = pearson_correlation(person,other)  #Similarity column

        # ignore scores of zero or lower
        if sim <=0:
            continue
        for item in dataset[other]:

            # only score movies i haven't seen yet
            if item not in dataset[person].keys():

                # Similarity * Score
                totals.setdefault(item,0)
                totals[item]= totals[item]+dataset[other][item]*sim

                # sum of similarities
                simSums.setdefault(item,0)
                simSums[item]= simSums[item] + sim    # We could just use the totals to calculate
                # the rankings, but then a movie reviewed by
                # more people would have a big advantage.
                # To correct for this you need to divide by the sum of
                # all the similraties for persons that reviewd that movie
                # (the Sim.Sum row in the table)
    # Create the normalized list
    rankings = [(total/simSums[item], item) for item , total in totals.items()]
    rankings.sort()
    rankings.reverse()
    print rankings
    # returns the recommended items
   # recommendations_list = [recommended_item for score,recommend_item in rankings]

user_recommendations('Toby')


