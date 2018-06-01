import csv
import time
import pandas as pd
import numpy as np
import re

print("Welcome to the 'De-Identification Control Layer' (version 0.1) - An interactive prototype by milhou5")
print("You can find me here https://github.com/milhou5 and here https://twitter.com/paddy_cass")
print('')
print('This program is designed to provide a practical demonstration of how de-identification of datasets can be achieved using the principle of K-Anonymity. Please see readme for further information and data specification.')
print('')
print('Data exposed to the control layer will undergo the following processes:')
print('1. File analysis.')
print('2. Classify identifying, quasi-identifying and sensitive attributes.')
print("3. Apply the 'generalisation technique'.")
print("4. Apply the 'suppression technique'.")
print('5. Confirm K-Aanonymity has been achieved and output de-identified dataset.')
print('')

attributes = []
records = []
identifiers = []
quasiidentifiers = []
sensitive = []

#check csv file exists in local directory
file = input("Please specify the name of your csv file including the extension '.csv' at the end; or to use the example file provided, please type 'example.csv': ")
print('')
try:
    f = open(file)
    f.close()
    rawdf = pd.read_csv(file)
    #read in the csv and create dataframe
    print('Loading csv file...')
    newdf = rawdf
    print('')
    time.sleep(2)
    print('This is the raw data')
    print('')
    print(rawdf)
    print('')
    time.sleep(2)
    print('File Summary:')
        
    with open(file) as csvfile:
        #create the csvreader object
        csvreader = csv.reader(csvfile, delimiter=',')
        #extract attribute names in the header row
        attributes = next(csvreader)
        #extract records
        next(csvfile)
        for record in csvreader:
            records.append(record)

        #print total number of rows without the heaader row
        print('Total no. of records: %d'%(csvreader.line_num))
        #print attributes from list
        print('The attributes are: ' + ', '.join(attribute for attribute in attributes))

except IOError:
    print('File is not accessible. Please check it exists in the local directory and re-run this program.')
    print('This program will close in 5 seconds')
    time.sleep(5)
    exit()



def attributeclassification():    
    #idenitfy the sensitive attributes
    print('SENSITIVE ATTRIBUTES')
    print("Sensitive attributes are data that is considered unknown to an attacker and must be protected. Sensitive information can include medical and salary information. Which attributes are considered sensitive in this dataset?")
    print('')
    for attribute in attributes:
        userInput = input("Is the attribute '" + attribute + "' sensitive? (Answer Y for Yes and N for No): ").upper()
        if userInput == 'Y':
            sensitive.append(attribute)
    time.sleep(1)
    print('')
    print('The sensitive attributes are: ' + ', '.join(sensitive for sensitive in sensitive))
    print('')
    time.sleep(2)

    #identify the identifiers
    print('IDENTIFIERS')
    print("Let's check whether we have any identifiers. An identifier is a type of attribute that can reveal an individual's identity without having to be combined with other attributes. For example; 'Name' and 'Social Security Number'.")
    print('')
    for attribute in attributes:
        userInput = input("Is the attribute '" + attribute + "' an identifier? (Answer Y for Yes and N for No): ").upper()
        if userInput == 'Y':
            identifiers.append(attribute)
    print('')
    time.sleep(1)
    print('The idenitfying attributes are: ' + ', '.join(identifier for identifier in identifiers))
    print('')
    time.sleep(2)

    #identify the quasi-identifiers
    print('QUASI-IDENTIFIERS')
    print("Let's check whether we have any quasi-identifiers. A quasi-identifier is an attribute that may be known by an attacker; such as 'Post Code' and 'Date of Birth'. These attributes can be combined in an effort to reveal the identity of an individual.")
    print('')
    for attribute in attributes:
        userInput = input("Is the attribute '" + attribute + "' a quasi-identifier? (Answer Y for Yes and N for No): ").upper()
        if userInput == 'Y':
            quasiidentifiers.append(attribute)
    print('')
    time.sleep(1)
    print('The quasi-identifier attributes are: ' + ', '.join(quasiidentifier for quasiidentifier in quasiidentifiers))
    print('')
    time.sleep(2)

#call the attributeclassification function
print('')
attributeclassification()

    
#Apply generalisation technique to quasi-identifiers
def generalisation():
    print('THE GENERALISATION TECHNIQUE')
    print('For some identifying and quasi-identifying attributes, the generalisation technique can be used to reduce the identifying quality of an attribute enough to allow for k-level anonymity. This technique avoids total information loss caused when an attribute has to be completely supressed from a dataset.')
    print('')
    for identifier in identifiers:
        if identifier == 'phone':
            print("It looks like we have a 'phone' attribute")
            print("We can apply the generalisation technique to the phone values by replacing the number value with a 'Mobile' or 'Landline' value.")
            newdf['phone'] = newdf['phone'].astype(str)
            newdf['phone'].replace('^4.*','Mobile', inplace=True, regex=True)
            newdf['phone'].replace('^(.(?<!Mobile))*?$','Landline', inplace=True, regex=True)
            print('')
            input('Press ENTER key to continue')
            print(newdf)
            print('')

    for quasiidentifier in quasiidentifiers:
        if quasiidentifier == 'post_code':
            print("We have a 'post_code' attribute")
            print("Let's apply the generalisation technique to the 'post_code' attribute.")
            print('')
            input('Press ENTER key to continue')

            newdf['post_code'] = newdf['post_code'].astype(str)
            newdf['post_code'].replace(r'.{1,2}$', '**', inplace=True, regex=True)
            print(newdf)
            print('')

    for quasiidentifier in quasiidentifiers:
        if quasiidentifier == 'dob':
            print("We have a 'dob' attribute")
            print("Let's apply the generalisation technique to the 'dob' attribute as well so only the birth year is shown.")
            print('')
            input('Press ENTER key to continue')
            
            newdf['dob'] = pd.to_datetime(newdf.dob)
            newdf['dob'] = newdf.dob.dt.year
            print(newdf)
            print('')
        
#export updated data set to csv file
def export():
    print('Congratulations! Your data set has been anonymised.')
    createfile = input("Would you like the de-identified data set be output to a csv file? (Answer Y for Yes and N for No): ").upper()

    if createfile == 'Y':
        newdf.to_csv('output.csv')
        print('')
        print("File has been created as 'output.csv' in the local directory.")
        print('Goodbye.')
        time.sleep(10)
    else:
        print('')
        print('Goodbye')
        time.sleep(10)
        
#call the generalisation function
generalisation()

#Supress the identifying attributes
print('THE SUPRESSION TECHNIQUE')
print('For those identifying and quasi-identifying attributes that we cannot apply the generalisation technique to, we can apply the supression technique to completely remove the value from the data set. For now, we will apply this technique to the identifiers only.')
print('')
input('Press ENTER key to continue')

def kcheck():
    print('K-ANONYMITY CHECK')
    kanon = input('Lets check whether we have achieved k-anonymity in this data set. Has the data set been sufficiently de-identified? (Answer Y for Yes and N for No): ').upper()
    if kanon == 'N':
        print('')
        supressattribute = input('Which attribute still needs to be supressed? ')
        if supressattribute in attributes:
            identifiers.append(supressattribute)
            supression()
        else:
            print('')
            print("There is no attribute by that name. Please try again.")
            print('')
            kcheck()
        
    else:
        print('')
        export()
        
def supression():
    for id_ in identifiers:
        if id_ != 'phone' and id_ != 'post_code' and id_ != 'dob':
            newdf[id_] = '***'

    print(newdf)
    print('')
    kcheck()
    
#call the supression function
print('')
supression()
