import numpy as np
import pandas as pd
from faker import Faker
from sklearn import tree
import matplotlib.pyplot as plt
from loguru import logger as lg


DATASET_ROWS = 100

def generate_data(num_rows:int):
    
    """
    Assessment 1 (If yes to all questions, proceed to Assessment 2):
    Question 1 - In the past 3 months, have you had any episodes of binge eating? (eating a much larger amount of food than most people would eat in the same period of time)
    Question 2 - Do you feel distressed or have any kind of suffering when you have these episodes?
    Question 3 - Do you feel like you lose control over your intake during episodes?
    Question 4 - After episodes of excessive drinking, do you usually induce vomiting, use medication or exercise to control your body weight?

    Assessment 2 (If yes to 3 or more questions, possible diagnosis of TCA):
    Question 5 - During the binge drinking episode, do you eat more quickly than normal?
    Question 6 - During the binge drinking episode, do you eat until you feel uncomfortably full?
    Question 7 - During the binge drinking episode, do you eat large amounts, even when you're not hungry?
    Question 8 - During the binge drinking episode, do you eat alone because you are ashamed of how much you are eating?
    Question 9 - During the binge drinking episode, do you feel disgusted, depressed or guilty afterwards?
    """
        
    # Initialize Faker
    fake = Faker()
    
    # Generate data using Faker
    data = {
        'question1':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question2':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question3':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question4':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question5':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question6':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question7':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question8':[fake.random_int(min=0, max=1) for row in range(num_rows)],
        'question9':[fake.random_int(min=0, max=1) for row in range(num_rows)]
    }
    
    return data

def create_valid_df():
    
    try:
        
        while True:
            
            # Get data
            data = generate_data(DATASET_ROWS)
            
            # Create DataFrame
            df_tca = pd.DataFrame(data)
            
            # Get list of columns
            # ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9']
            assessments = df_tca.columns.tolist()

            # Diganosis Logic
            df_tca['tca_diagnosis'] = np.where(((df_tca[assessments[:4]].sum(axis=1)) == 4) & ((df_tca[assessments[4:]].sum(axis=1)) >= 3), 1, 0)
            
            tca_cases = df_tca.loc[df_tca['tca_diagnosis'] == 1]
            
            if not tca_cases.empty:
                lg.success("Data frame created successfully")
                lg.success("Diagnosis completed successfully")
                
                # Display TCA Cases
                lg.info(f"TCA cases:\n{tca_cases}")
                break
        
        return df_tca, assessments
        
    except KeyError as e:
        raise(e)

if __name__ == '__main__':    
    
    df_tca, assessments = create_valid_df()
    
    # Defining model variables
    x = df_tca[assessments]
    y = df_tca['tca_diagnosis']  
    
    # Run model
    clf = tree.DecisionTreeClassifier()
    clf.fit(x,y)


    # Plot Results
    tree.plot_tree(clf, feature_names=assessments, class_names=['No', 'Yes'], filled=True)
    plt.savefig('tca_tree_decision.png')

# Tests

# # Test1: Success
# print(clf.predict([[1,1,1,1,1,1,1,1,1]]))

# # Test2: Success
# print(clf.predict([[1,1,1,1,1,1,1,0,0]]))

# # Test1: Faild
# print(clf.predict([[1,1,1,1,1,1,0,0,0]]))

# # Test1: Faild
# print(clf.predict([[1,0,1,1,1,1,1,1,1]]))