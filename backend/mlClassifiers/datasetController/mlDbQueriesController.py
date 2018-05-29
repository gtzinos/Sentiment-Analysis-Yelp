from backend.dbQueries.databaseTable import DatabaseTable
from backend.dbQueries.restaurants import Restaurants as restaurantsQueryCreator
from backend.dbQueries.users import Users as usersQueryCreator
from backend.dbQueries.reviews import Reviews as reviewsQueryCreator


class ML_DatasetCreator(DatabaseTable):

  def __init__(self, reviewTableName, userTableName, restaurantTableName):

    DatabaseTable.__init__(self, reviewTableName=reviewTableName,
                           userTableName=userTableName,
                           restaurantTableName=restaurantTableName)


  def get_filtered_ml_reviews(self, db, typeOfRestaurant):

    goodReviewersList = usersQueryCreator.get_goodUsers_list(db=db, userTableName=self.userTableName)

    japaneseRestaurantList = restaurantsQueryCreator.get_restaurant_list(db=db,
                                                                         restaurant_type=typeOfRestaurant,
                                                                         restaurantTableName=self.restaurantTableName)

    filteredReviews = reviewsQueryCreator.get_goodUser_reviews(db=db, reviewTableName=self.reviewTableName,
                                                               goodReviewersList=goodReviewersList,
                                                               restaurantList=japaneseRestaurantList)

    return filteredReviews


