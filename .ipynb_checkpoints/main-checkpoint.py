#The purpose of this project is to analyze survey data
#from StackOverflow 

#Importing pandas for data analysis.
import pandas as pd
#Reading the csv file for data analysis
df = pd.read_csv("survey_results_public.csv")
#Checks if this Python file is the main execution file, and executes the code within the branch statement.
if __name__=="__main__":
    #Cleaning data.
    #This section fills missing data in numeric columns with zeros.
    df["Age"].fillna(0, inplace=True)
    df["Age1stCode"].fillna(0, inplace=True)
    df["WorkWeekHrs"].fillna(0,inplace=True)
    df["YearsCode"].fillna(0, inplace=True)
    df["YearsCodePro"].fillna(0, inplace=True)
    df["CompTotal"].fillna(0, inplace=True)
    df["ConvertedComp"].fillna(0, inplace=True)
    #This loop fills missing data in the remaining columns with missing
    for col in df.columns:
        df[col].fillna("Missing", inplace=True)
    
    
    #Getting top 3 countries with the highest number
    #of respondents who indicated they developers by trade

    #Filters out rows that do not contain developers.
    filt = (df["MainBranch"]=="I am a developer by profession")
    
    #Getting counts of each country 
    unique_values = df.loc[filt]
    #Results containing list of countries
    res = unique_values["Country"].value_counts()
    print(res.head())
    #Getting number of hobbyists
    hobbyist_values = df["Hobbyist"].value_counts()
    print(hobbyist_values)
    #Gathering most popular databases
    database_values = df["DatabaseWorkedWith"]
    

    #The following section goes through each row in the database worked with column
    #There are multiple responses per person, so 
    # I split them into a new dataframe and count each occurrence to determine the most popular databases are. 
    all_database_results = database_values.str.split(";").explode()
    print(all_database_results.value_counts())

    #The following section goes through each row in the languages worked with column
    #There are multiple responses per person, so 
    # I split them into a new dataframe and count each occurrence to determine the most popular languages are. 

    languages = df["LanguageWorkedWith"]
    all_languages_results = languages.str.split(";").explode()
    print(all_languages_results.value_counts().head())

    #Gathering what OS used by respondents
    os_values = df["OpSys"]
    filtered_os_values = os_values.str.split(";").explode()
    print(filtered_os_values.value_counts())
    print(df["DevType"])
    #Obtaining education levels.
    education_level = df["EdLevel"].value_counts()
    print(education_level)

    print(df.groupby(["YearsCodePro"]).mean())
    





