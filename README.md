# collaborative_recommendation
collaborative recommendation application using Python and KNN algorithm 

# Requirements:
    The project requires a dataset from the company that includes information about books, users, and book ratings. To make separation easier, data should be split by a unique delimiter.
        (a)	Books.csv: ISBN, book-title, book-author, year-of-publication, publisher
        (b)	Users.csv: user-ID, location, age
        (c)	Book_Ratings.csv: user-ID ISBN, book-rating

# Program is consist of 8 Main modules:	
    1.	similarities.py
    2.	load_data_set.py
    3.	recommend_on_books.py
    4.	recommend_on_users.py
    5.	main_program.py
    6.	test.py
    7.	knn_model_1 (KNeighborsClassifier)
    8.	knn_model_2 (sklearn.neighbors NearestNeighbors)


# Program Execution:
    1.	Unzip the folder contents
    2.	Open a python script
    3.	Import (test.py) => import test
    4.	Create an object of Test (): class => t = test.Test()
    5.	Run the process by executing => t.test()
# Additional Information: Two test cases included
    1.	For Recommendation using User-ID use => t.test_case()
    Test case will run using 
    User-ID: 276704, similarity function = 'pearson_correlation', threshold= 10
    2.	For Recommendation using ISBN use => t.test_case_2()
    Test case will run using 
    ISBN: 034544003X, similarity function = 'pearson_correlation', threshold= 10

