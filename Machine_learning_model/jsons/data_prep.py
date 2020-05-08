# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
client = pymongo.MongoClient(""mongodb://)
# client = pymongo.MongoClient(
 #   "mongodb://fouthpillar:pillar@cluster0-shard-00-00-lv2tm.mongodb.net:27017,cluster0-shard-00-01-lv2tm.mongodb.net:27017,cluster0-shard-00-02-lv2tm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
with client:
    db = client['newsdb']
    # collection = db['feed_ndtv']

collection = db['feed_ndtv']
myquery = {
    "_id": {"$regex": "/world-news/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics.")

myquery = {
    "_id": {"$regex": "/business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : business.")

myquery = {
    "_id": {"$regex": "/science/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : technology.")

myquery = {
    "_id": {"$regex": "/elections/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics.")

myquery = {
    "_id": {"$regex": "/sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : sports.")

myquery = {
    "_id": {"$regex": "/education/"}}
newvalues = {"$set": {"category": "education"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : education.")

myquery = {
    "_id": {"$regex": "/cricket/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : sports(cricket).")

myquery = {
    "_id": {"$regex": "/entertainment/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : entertainment.")

myquery = {
    "_id": {"$regex": "/gadgets.ndtv.com/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : technology.")

myquery = {
    "_id": {"$regex": "/sports.ndtv.com/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : sports.")

myquery = {
    "_id": {"$regex": "/movies.ndtv.com/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : entertainment.")

myquery = {
    "_id": {"$regex": "/doctor.ndtv.com/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : lifestyle.")

myquery = {
    "_id": {"$regex": "/swachhindia.ndtv.com/"}}
newvalues = {"$set": {"category": "pollution"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : pollution.")

myquery = {
    "_id": {"$regex": "/swirlster.ndtv.com/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : lifestyle.")

myquery = {
    "_id": {"$regex": "/food.ndtv.com/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : lifestyle.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : politics.")


myquery = {
    "_id": {"$regex": "/health/"}}
newvalues = {"$set": {"category": "health"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in ndtv : health.")

myquery = {
    "_id": {"$regex": "^https://khabar.ndtv.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted : khabar.")

myquery = {
    "_id": {"$regex": "/tamil/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted : tamil.")


""" IndiaTv """


collection = db['feed_indiatv']

myquery = {
    "_id": {"$regex": "/lifestyle/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : lifestyle.")

myquery = {
    "_id": {"$regex": "/sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : sports.")

myquery = {
    "_id": {"$regex": "/entertainment/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : entertainment.")

myquery = {
    "_id": {"$regex": "/elections/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : politics.")

myquery = {
    "_id": {"$regex": "/education/"}}
newvalues = {"$set": {"category": "education"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : education.")

myquery = {
    "_id": {"$regex": "/crime/"}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : crime.")

myquery = {
    "_id": {"$regex": "/politics/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : politics.")

myquery = {
    "_id": {"$regex": "/science/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : technology.")


myquery = {
    "_id": {"$regex": "/business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : business.")

myquery = {
    "_id": {"$regex": "/technology/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : technology.")

myquery = {
    "_id": {"$regex": "/jobs/"}}
newvalues = {"$set": {"category": "employment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : employment.")

myquery = {
    "_id": {"$regex": "/world-"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : world.")

myquery = {
    "_id": {"$regex": "/entertainment-"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : entertainment.")

myquery = {
    "_id": {"$regex": "/sports-"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : sports.")

myquery = {
    "_id": {"$regex": "fashion-lifestyle-"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indiatv : entertainment.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in IndiaTv : politics.")


myquery = {
    "_id": {"$regex": "/hindi.indiatvnews.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted : hindi.")


"""indianExpress"""
collection = db['feed_indianexpress']

myquery = {
    "_id": {"$regex": "/lok-sabha-elections"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : politics(lok sabha).")

myquery = {
    "_id": {"$regex": "/elections/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : politics.")

myquery = {
    "_id": {"$regex": "/entertainment/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : entertainment.")

myquery = {
    "_id": {"$regex": "/lifestyle/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : lifestyle.")

myquery = {
    "_id": {"$regex": "/technology/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : technology.")

myquery = {
    "_id": {"$regex": "/sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : sports.")

myquery = {
    "_id": {"$regex": "/world-news/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : world.")

myquery = {
    "_id": {"$regex": "/world/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : world.")

myquery = {
    "_id": {"$regex": "/education/"}}
newvalues = {"$set": {"category": "education"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : education.")

myquery = {
    "_id": {"$regex": "/business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : business.")

myquery = {
    "_id": {"$regex": "/entertainment-gallery/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : entertainment.")


myquery = {
    "_id": {"$regex": "/sports-gallery/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : sports.")

myquery = {
    "_id": {"$regex": "/health-fitness/"}}
newvalues = {"$set": {"category": "health"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : health.")

myquery = {
    "_id": {"$regex": "/lifestyle-video/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : lifestyle.")

myquery = {
    "_id": {"$regex": "/sports-video/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : sports.")


myquery = {
    "_id": {"$regex": "/jobs-news-gallery/"}}
newvalues = {"$set": {"category": "employment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : employment.")

myquery = {
    "_id": {"$regex": "/lifestyle-gallery/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : entertainment.")

myquery = {
    "_id": {"$regex": "/express-sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : sports.")

myquery = {
    "_id": {"$regex": "/entertainment-video/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : entertainment.")

myquery = {
    "_id": {"$regex": "/tech-video/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : technology.")

myquery = {
    "_id": {"$regex": "/elections-video/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : politics.")

myquery = {
    "_id": {"$regex": "/auto-video/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : technology.")

myquery = {
    "_id": {"$regex": "/jobs/"}}
newvalues = {"$set": {"category": "employment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : employment.")

myquery = {
    "_id": {"$regex": "/pakistan/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianexpress : world.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : accident.")

myquery = {
    "headline": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics.")

myquery = {
    "_id": {"$regex": "/malayalam.indianexpress.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :malayalam.")

myquery = {
    "_id": {"$regex": "/www.loksatta.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :loksatta.")

myquery = {
    "_id": {"$regex": "/tamil.indianexpress.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :tamil.")

myquery = {
    "_id": {"$regex": "/bengali.indianexpress.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :bengali.")

myquery = {
    "_id": {"$regex": "/www.jansatta.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :jansatta.")

myquery = {
    "_id": {"$regex": "/express-sunday-eye/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :express-sunday-eye.")


""" firstpost """
collection = db['feed_firstpost']

myquery = {
    "_id": {"$regex": "/politics/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "_id": {"$regex": "/sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : sports.")

myquery = {
    "_id": {"$regex": "/firstcricket/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : sports.")

myquery = {
    "_id": {"$regex": "/tech/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : technology.")

myquery = {
    "_id": {"$regex": "/entertainment/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : entertainment.")

myquery = {
    "_id": {"$regex": "/bollywood/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : entertainment.")

myquery = {
    "_id": {"$regex": "/world/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : world.")

myquery = {
    "_id": {"$regex": "/business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : business.")

myquery = {
    "_id": {"$regex": "/living/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : lifestyle.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in indianExpress : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")


"""DNA"""

collection = db['feed_dna']

myquery = {
    "_id": {"$regex": "/bollywood/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : entertainment.")

myquery = {
    "_id": {"$regex": "/entertainment/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : entertainment.")

myquery = {
    "_id": {"$regex": "/technology/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : technology.")

myquery = {
    "_id": {"$regex": "/television/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : entertainment.")

myquery = {
    "_id": {"$regex": "/science/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : technology.")

myquery = {
    "_id": {"$regex": "/education/"}}
newvalues = {"$set": {"category": "education"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : education.")

myquery = {
    "_id": {"$regex": "/sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : sports.")

myquery = {
    "_id": {"$regex": "/health/"}}
newvalues = {"$set": {"category": "health"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : health.")

myquery = {
    "_id": {"$regex": "/business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : business.")

myquery = {
    "_id": {"$regex": "/cricket/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : sports.")

myquery = {
    "_id": {"$regex": "/lifestyle/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : lifestyle.")

myquery = {
    "_id": {"$regex": "/hollywood/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : entertainment.")

myquery = {
    "_id": {"$regex": "/world/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : world.")


myquery = {
    "_id": {"$regex": "/personal-finance/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in DNA : business.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in firstpost : politics.")


"""News18"""
collection = db['feed_news18']

myquery = {
    "_id": {"$regex": "/politics/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics.")

myquery = {
    "_id": {"$regex": "/lifestyle-2/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : lifestyle.")

myquery = {
    "_id": {"$regex": "/world/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : world.")

myquery = {
    "_id": {"$regex": "/other-sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : sports.")

myquery = {
    "_id": {"$regex": "/football/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : sports.")

myquery = {
    "_id": {"$regex": "/hockey/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : sports.")

myquery = {
    "_id": {"$regex": "/badminton/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : sports.")

myquery = {
    "_id": {"$regex": "/footballnext/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : sports.")

myquery = {
    "_id": {"$regex": "/cricketnext/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : sports.")

myquery = {
    "_id": {"$regex": "/movies/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : entertainment.")

myquery = {
    "_id": {"$regex": "/tv/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : entertainment.")

myquery = {
    "_id": {"$regex": "/tech/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : technology.")

myquery = {
    "_id": {"$regex": "/auto/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : technology.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in news18 : politics.")

"""oneIndia"""
collection = db["feed_oneindia"]


myquery = {
    "_id": {"$regex": "www.goodreturns.in"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : sports.")

myquery = {
    "_id": {"$regex": "www.mykhel.com"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : sports.")

myquery = {
    "_id": {"$regex": "cb.mykhel.com"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : sports.")

myquery = {
    "_id": {"$regex": "/international/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : world.")

myquery = {
    "_id": {"$regex": "/hindi.oneindia.com/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :hindi.")

myquery = {
    "_id": {"$regex": "www.drivespark.com"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : technology.")

myquery = {
    "_id": {"$regex": "www.gizbot.com"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : technology.")

myquery = {
    "_id": {"$regex": "www.careerindia.com"}}
newvalues = {"$set": {"category": "employment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : employment.")

myquery = {
    "_id": {"$regex": "www.boldsky.com"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : entertainment.")


myquery = {
    "_id": {"$regex": "/www.filmibeat.com"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : entertainment.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in oneIndia : politics.")


"""republic"""

collection = db['feed_republic']

myquery = {
    "_id": {"$regex": "/election-news/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")

myquery = {
    "_id": {"$regex": "/technology-news/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : technology.")

myquery = {
    "_id": {"$regex": "/entertainment-news/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : entertainment.")

myquery = {
    "_id": {"$regex": "/sports-news/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : sports.")

myquery = {
    "_id": {"$regex": "/world-news/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : world.")

myquery = {
    "_id": {"$regex": "/lifestyle/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : lifestyle.")

myquery = {
    "_id": {"$regex": "/elections/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in republic : politics.")

""""the hindu"""

collection = db['feed_thehindu']

myquery = {
    "_id": {"$regex": "/elections/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "_id": {"$regex": "/sport/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : sport.")


myquery = {
    "_id": {"$regex": "/business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : business.")

myquery = {
    "_id": {"$regex": "/www.thehindubusinessline.com/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : business.")

myquery = {
    "_id": {"$regex": "/sci-tech/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : technology.")

myquery = {
    "_id": {"$regex": "/entertainment/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : entertainment.")

myquery = {
    "_id": {"$regex": "/life-and-style/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : lifestyle.")

myquery = {
    "_id": {"$regex": "/society/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : lifestyle.")


myquery = {
    "_id": {"$regex": "/international/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : world.")

myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")


"""zee"""

collection = db['feed_zeenews']

myquery = {
    "_id": {"$regex": "/technology/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : technology.")

myquery = {
    "_id": {"$regex": "/education/"}}
newvalues = {"$set": {"category": "education"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : education.")

myquery = {
    "_id": {"$regex": "/assembly-elections/"}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : politics.")

myquery = {
    "_id": {"$regex": "/bollywood/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : entertainment.")

myquery = {
    "_id": {"$regex": "/bhojpuri/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : entertainment.")

myquery = {
    "_id": {"$regex": "/hollywood/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : entertainment.")

myquery = {
    "_id": {"$regex": "/music/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : entertainment.")

myquery = {
    "_id": {"$regex": "/people/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : entertainment.")

myquery = {
    "_id": {"$regex": "/television/"}}
newvalues = {"$set": {"category": "entertainment"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : entertainment.")

myquery = {
    "_id": {"$regex": "/cricket/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : sports.")

myquery = {
    "_id": {"$regex": "/world/"}}
newvalues = {"$set": {"category": "world"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : world.")

myquery = {
    "_id": {"$regex": "/automobile/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : technology.")

myquery = {
    "_id": {"$regex": "/personal-finance/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : business.")

myquery = {
    "_id": {"$regex": "/companies/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : business.")

myquery = {
    "_id": {"$regex": "/economy/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : business.")

myquery = {
    "_id": {"$regex": "/real-estate/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : business.")

myquery = {
    "_id": {"$regex": "/international-business/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : business.")


myquery = {
    "_id": {"$regex": "/markets/"}}
newvalues = {"$set": {"category": "business"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : business.")

myquery = {
    "_id": {"$regex": "/science/"}}
newvalues = {"$set": {"category": "technology"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : technology.")

myquery = {
    "_id": {"$regex": "/health/"}}
newvalues = {"$set": {"category": "health"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : health.")

myquery = {
    "_id": {"$regex": "/other-sports/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : sports.")

myquery = {
    "_id": {"$regex": "/hockey/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : sports.")

myquery = {
    "_id": {"$regex": "/badminton/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : sports.")

myquery = {
    "_id": {"$regex": "/football/"}}
newvalues = {"$set": {"category": "sports"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : sports.")

myquery = {
    "_id": {"$regex": "/culture/"}}
newvalues = {"$set": {"category": "lifestyle"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : lifestyle.")

myquery = {
    "_id": {"$regex": "/jammu-and-kashmir/"}}
newvalues = {"$set": {"category": "terrorism"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in zee : terrorism.")

myquery = {
    "_id": {"$regex": "/marathi/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :marathi.")

myquery = {
    "_id": {"$regex": "/hindi/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :hindi.")

myquery = {
    "_id": {"$regex": "/bengali/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :bengali.")

myquery = {
    "_id": {"$regex": "/tamil/"}}
x = collection.delete_many(myquery)
print(x.deleted_count, " documents deleted :tamil.")


myquery = {
    "headline": {"$regex": "gandhi", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics(gandhi).")

myquery = {
    "headline": {"$regex": "bjp", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics(bjp).")

myquery = {
    "headline": {"$regex": "congress", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics(congress).")

myquery = {
    "headline": {"$regex": "rape", "$options": 'i'}}
newvalues = {"$set": {"category": "crime"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : crime(rape).")

myquery = {
    "headline": {"$regex": "poll", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "headline": {"$regex": "manifesto", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")


myquery = {
    "headline": {"$regex": "vote", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "headline": {"$regex": "Cyclone", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : accident.")

myquery = {
    "headline": {"$regex": "fani", "$options": 'i'}}
newvalues = {"$set": {"category": "accident"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : accident.")

myquery = {
    "_id": {"$regex": "lok", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

myquery = {
    "_id": {"$regex": "election", "$options": 'i'}}
newvalues = {"$set": {"category": "politics"}}
x = collection.update_many(myquery, newvalues)
print(x.modified_count, "documents updated in thehindu : politics.")

# """
# {"headline" : {$regex: "modi", $options: 'i'}}
# myquery = {
#     "_id": {"$regex": "^www.dnaindia.com/cricket/"}}
# newvalues = {"$set": {"category": "sports"}}
# x = collection.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")
# x = collection.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")
# "$options": 'i'
#
# """
# myquery = {"headline": {"$regex": "modi", "$options": 'i'}}


client.close()
