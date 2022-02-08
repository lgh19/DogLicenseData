import pandas as pd

#function outputs a csv file with each zip code's most popular dog name
def dog_names_by_zip(file,year):
    df = pd.read_csv(file)
    finalDict = {}
    zips = []
    
    #makes array of zips 
    for index, row in df.iterrows():
        if row.OwnerZip not in zips:
            zips.append(row.OwnerZip)
            
    #for each zip code a data frame of entries from only that zip code is created (new_df)
    for z in zips:
        new_df = df[df["OwnerZip"] == z]
        temp_dict = {}
        
        #iterates through new_df and puts each dog name and number of times it appears in hash table
        #key = dog name and value = number of times recorded
        for index, row in new_df.iterrows():
            temp_dog_name = row.DogName
            if temp_dog_name in temp_dict:
                temp_dict[temp_dog_name]+=1
            else:
                temp_dict[temp_dog_name] = 1
                
        highest = 0
        popular = ""
        
        #iterates through hash table and finds dog name with highest occurrance
        for key, value in temp_dict.items():
            if temp_dict[key] > highest:
                popular = key
                highest = temp_dict[key]
        #puts the zip code and most popular dog name into finalDict
        finalDict[z] = popular
    
    #creates a file to export the csv
    output_file_name = "dog_names_" + str(year) + ".csv"
    end_file = open(output_file_name, "w")
    writer = csv.writer(end_file)
    #writes dictionary contents to file
    writer.writerow(['ZipCode','DogName'])
    for key, value in finalDict.items():
        writer.writerow([key, value])

    end_file.close()

#outputs a csv file with each zip code's most popular dog breed
def dog_breeds_by_zip(file,year):
    df = pd.read_csv(file)
    finalDict = {}
    zips = []
    #makes array of zips 
    for index, row in df.iterrows():
        if row.OwnerZip not in zips:
            zips.append(row.OwnerZip)
    #for each zip code a data frame of entries from only that zip code is created (new_df)
    for z in zips:
        new_df = df[df["OwnerZip"] == z]
        temp_dict = {}
        #iterates through new_dict and puts dog breed and number of times it appears in hash table
        #as key = breed and value = number of times recorded
        for index, row in new_df.iterrows():
            temp_dog_breed = row.Breed
            if temp_dog_breed in temp_dict:
                temp_dict[temp_dog_breed]+=1
            else:
                temp_dict[temp_dog_breed] = 1
                
        highest = 0
        popular = ""
        #iterates through has table and finds dog breed with highest occurrance
        for key, value in temp_dict.items():
            if temp_dict[key] > highest:
                popular = key
                highest = temp_dict[key]
        #puts the zip code and most popular dog breed into finalDict
        finalDict[z] = popular
    
    #creates a file to export the csv
    output_file_name = "dog_breeds_" + str(year) + ".csv"
    end_file = open(output_file_name, "w")
    writer = csv.writer(end_file)
    #writes dictionary contents to file
    writer.writerow(['ZipCode','DogBreed'])
    for key, value in finalDict.items():
        writer.writerow([key, value])

    end_file.close()
    
#calls dog_names_by_zip() and dog_breeds_by_zip() and passes in data and year
def call_dog_license_functions():
    #dog names
    dog_names_by_zip("dog_license_2008.csv", 2008)
    dog_names_by_zip("dog_license_2009.csv", 2009)
    dog_names_by_zip("dog_license_2010.csv", 2010)
    dog_names_by_zip("dog_license_2011.csv", 2011)
    dog_names_by_zip("dog_license_2012.csv", 2012)
    dog_names_by_zip("dog_license_2013.csv", 2013)
    dog_names_by_zip("dog_license_2014.csv", 2014)
    dog_names_by_zip("dog_license_2015.csv", 2015)
    dog_names_by_zip("dog_license_2016.csv", 2016)
    dog_names_by_zip("dog_license_2017.csv", 2017)
    dog_names_by_zip("dog_license_2018.csv", 2018)
    dog_names_by_zip("dog_license_2019.csv", 2019)
    dog_names_by_zip("2020_dog_licenses.csv", 2020)
    dog_names_by_zip("dog_license_2021.csv", 2021)
    dog_names_by_zip("dog_license_2022.csv", 2022)
    #dog breeds
    dog_breeds_by_zip("dog_license_2008.csv", 2008)
    dog_breeds_by_zip("dog_license_2009.csv", 2009)
    dog_breeds_by_zip("dog_license_2010.csv", 2010)
    dog_breeds_by_zip("dog_license_2011.csv", 2011)
    dog_breeds_by_zip("dog_license_2012.csv", 2012)
    dog_breeds_by_zip("dog_license_2013.csv", 2013)
    dog_breeds_by_zip("dog_license_2014.csv", 2014)
    dog_breeds_by_zip("dog_license_2015.csv", 2015)
    dog_breeds_by_zip("dog_license_2016.csv", 2016)
    dog_breeds_by_zip("dog_license_2017.csv", 2017)
    dog_breeds_by_zip("dog_license_2018.csv", 2018)
    dog_breeds_by_zip("dog_license_2019.csv", 2019)
    dog_breeds_by_zip("2020_dog_licenses.csv", 2020)
    dog_breeds_by_zip("dog_license_2021.csv", 2021)
    dog_breeds_by_zip("dog_license_2022.csv", 2022)
    
call_dog_license_functions()
