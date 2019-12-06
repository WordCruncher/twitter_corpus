import datetime
import glob
import json
import math
import os
import re
import subprocess
import sys
subprocess.run([sys.executable, '-m', 'pip', 'install', '--user', 'textblob'])
from textblob import TextBlob


calendarDict = {'1': 'January', '2': 'February', '3': 'March', '4': 'April',
                '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September',
                '10': 'October', '11': 'November', '12': 'December'}

directory = os.path.dirname(os.path.realpath(__file__))
directory = re.sub(r'\\', r'/', directory)
directory = directory + '/'

json_files = glob.glob(directory + '*.json')

etax = 'WCr-Tweets.etax'

etax_file = open(directory + etax, 'w').close()
etax_file = open(directory + etax, 'a', encoding='utf-8')

# This is content important for WordCruncher. Do not change.
print('<?xml version="1.0" encoding="utf-8"?>', file=etax_file)
print('<etax id="{d4643d93-2459-49a8-bf2e-6fdf85659bb7}">', file=etax_file)
print('<sifx>', file=etax_file)
print('  <DS clrHilite="white;dkgray" clrHit="white;29,161,242" clrReader="29,161,242;23,114,169" clrRef="blue;white" clrTxt="black;white" dir="ltr" idxOff="script" lnWidth="t:23040,14400" mrgL="t:120,60" mrgR="t:120,60"/>', file=etax_file)

print('\n  <PS st="Normal" tSt="Normal" dir="ltr" just="full" spA="p:6"/>', file=etax_file)
print('  <PS st="user" dir="ltr" just="full" spB="p:6"/>', file=etax_file)
print('  <PS st="RT" tSt="RT" dir="ltr" just="full" spB="p:6"/>', file=etax_file)

print('\n  <LEX st="Tweets" id="en" chrBrk="—" chrNobrk="\':/"/>', file=etax_file)
print('  <LEX st="Retweets" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Creation Date" tSt="cd" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Favorited Count" tSt="m" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Hashtags" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Hashtag Counts" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="@References" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Hyperlinks" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Language" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Location" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Sentiment Analysis" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Subjective Analysis" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Username" tSt="U" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="User Description" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="User Followers" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="User Post Count" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Retweeted Count" tSt="m" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Screen Name" tSt="sn" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)
print('  <LEX st="Metadata" tSt="m" id="en" chrBrk="—" chrNobrk="\'"/>', file=etax_file)

print('\n  <TS st="Normal" lexSt="Tweets" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman"/>', file=etax_file)
print('  <TS st="RT" lexSt="Retweets" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman"/>', file=etax_file)
print('  <TS st="m" lexSt="Metadata" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" />', file=etax_file)
print('  <TS st="U" lexSt="Username" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" chrProp="bold"/>', file=etax_file)
print('  <TS st="sn" lexSt="Screen Name" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" />', file=etax_file)
print('  <TS st="cd" lexSt="Creation Date" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" />', file=etax_file)
print('  <TS st="HT" lexSt="Hashtags" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" />', file=etax_file)
print('  <TS st="AT" lexSt="@References" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" />', file=etax_file)
print('  <TS st="HTTP" lexSt="Hyperlinks" tHeight="p:12" clrTxt="0,0,0" fFace="Times New Roman" fFaceSm="Times New Roman" />', file=etax_file)

print('\n  <LVL code="u" name="User" plural="Users" sep=""/>', file=etax_file)
print('  <LVL code="y" name="Year" plural="Years" sep=": "/>', file=etax_file)
print('  <LVL code="m" name="Month" plural="Months" sep=" "/>', file=etax_file)
print('  <LVL code="d" name="Day" plural="Days" sep=" "/>', file=etax_file)
print('  <LVL code="s" name="Section" plural="Sections" sep=", Sect. "/>', file=etax_file)
print('  <LVL code="t" name="Tweet" plural="Tweets" sep=" "/>', file=etax_file)

print('\n  <ATTR code="H" lexSt="Metadata" name="Hashtag" plural="Hashtags" tagtype="H"/>', file=etax_file)
print('\n  <ATTR code="h" lexSt="Hashtag Counts" name="Hashtag Count" plural="Hashtag Counts" tagtype="h"/>', file=etax_file)
print('  <ATTR code="F" lexSt="User Followers" name="User Follower" plural="User Followers" tagtype="F"/>', file=etax_file)
print('  <ATTR code="P" lexSt="User Post Count" name="User Post Count" plural="User Post Counts" tagtype="P"/>', file=etax_file)
print('  <ATTR code="f" lexSt="Favorited Count" name="Favorited Count" plural="Favorited Counts" tagtype="f"/>', file=etax_file)
print('  <ATTR code="R" lexSt="Retweeted Count" name="Retweeted Count" plural="Retweeted Counts" tagtype="R"/>', file=etax_file)
print('  <ATTR code="S" lexSt="Sentiment Analysis" name="Sentiment Analysis" plural="Sentiment Analyses" tagtype="S"/>', file=etax_file)
print('  <ATTR code="s" lexSt="Subjective Analysis" name="Subjective Analysis" plural="Subjective Analyses" tagtype="s"/>', file=etax_file)

print('\n  <TAG code="H" name="Hashtag" plural="Hashtags"/>', file=etax_file)
print('  <TAG code="h" name="Hashtag Count" plural="Hashtag Counts"/>', file=etax_file)
print('  <TAG code="F" name="User Follower" plural="User Followers"/>', file=etax_file)
print('  <TAG code="P" name="User Post Count" plural="User Post Counts"/>', file=etax_file)
print('  <TAG code="f" name="Favorited Count" plural="Favorited Counts"/>', file=etax_file)
print('  <TAG code="R" name="Retweeted Count" plural="Retweeted Counts"/>', file=etax_file)
print('  <TAG code="S" name="Sentiment Analysis" plural="Sentiment Analyses"/>', file=etax_file)
print('  <TAG code="s" name="Subjective Analysis" plural="Sentiment Analyses"/>', file=etax_file)

print('</sifx>', file=etax_file)

print('<p just="center"><T st="m">Twitter Corpus</T></p>', file=etax_file)
print(f'<p><T st="m">This corpus was compiled on {datetime.datetime.today().strftime("%B %d, %Y")}</T></p>', file=etax_file)
print(f'<p><T st="m">Sentiment Analysis is a measurement for how positive a text is. The most positive text is 1.0 and the most negative is -1.0.</T></p>', file=etax_file)
print(f'<p><T st="m">Subjective Analysis is a measurement for how subjective a text is. The most subjective text is 1.0 and the most objective is 0.0.</T></p>', file=etax_file)
print(f'<p><T st="m"><b>Abbreviations</b>:</T></p>', file=etax_file)
print(F'<p><T st="m">RTF Ratio: Retweet to Follower Ratio. Take the total of the retweets and divide it by how many followers the person has. Log it and add 14.</T></p>', file=etax_file)
print(F'<p><T st="m">FTF Ratio: Favorite to Follower Ratio. Take the total of the favorited and divide it by how many followers the person has. Log it and add 14.</T></p>', file=etax_file)
# Cleans the tweet text generally. Removes unwanted lines, tabs, spaces, etc.


def cleaner(tweet):
    tweet = re.sub(r'[\n\t\r]', r' ', tweet)
    tweet = re.sub(r' {2,100}', r' ', tweet)
    tweet = re.sub(r'&', r'&amp;', tweet)
    tweet = re.sub(r' \+0000', r'', tweet)
    # These two remove @, #, and links in Twitter from being indexed.
    tweet = re.sub(r'([#][^\s]+?)(\s)', r'<T st="HT">\1</T>\2', tweet)
    tweet = re.sub(r'([@][^\s]+?)(\s)', r'<T st="AT">\1</T>\2', tweet)
    tweet = re.sub(r'(http[^\s]+?)(\s)', r'<T st="HTTP">\1</T>\2', tweet)
    tweet = re.sub(r'<T</T>', r'</T><T', tweet)
    return tweet

# Cleans the text, so that the sentiment analysis doesn't hit garbage emojis, characters, etc.


def sentiment_tweet(tweet):
    return ' '.join(re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', r' ', tweet).split())


def char_date(date):
    date = re.sub(r' ', r'<sp/>', date)
    date = re.sub(r'(\d{2}:\d{2}:\d{2})<sp/>(20\d{2})', r'\2 <sw>\1</sw>', date)
    return date


illegal_xml_chars = re.compile(u'[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]')


def escape_xml_illegal_chars(val, replacement='?'):
    if re.search(illegal_xml_chars, val):
        iBrk = 0
    return illegal_xml_chars.sub(replacement, val)


for i in json_files:
    dateDict = {}
    refDict = {}
    userDict = {}

    tweet_counter = 0
    section_counter = 1
    print(i)
    with open(i, 'r', encoding='utf-8') as fIn:
        my_input = fIn.read().splitlines()

        for tweet in my_input:
            tweet_counter += 1
            if (tweet_counter - 1) % 3000 == 0 and tweet_counter != 1:
                section_counter += 1
                print(f'<p><R ref="s,4:Section {section_counter}"/> </p>', file=etax_file)

            tweetDict = json.loads(tweet)

            # Collect the language of the tweet.
            language = tweetDict['lang']
            if language == 'und':
                language = 'undefined'

            # Collect creation date.
            creation_date = cleaner(tweetDict['created_at'])
            simple_date = re.sub(r'\w{3} (\w{3} \d{2}) \d{2}:\d{2}:\d{2} (\d{4})', r'\1 \2', creation_date)

            # Collect the user information.
            name = tweetDict['user']['name']
            screen_name = tweetDict['user']['screen_name']
            location = tweetDict['user']['location']
            user_followers = tweetDict['user']['followers_count']
            user_posts = tweetDict['user']['statuses_count']
            user_since = re.sub(r'\w{3} (\w{3} \d{2}) \d{2}:\d{2}:\d{2} \+0000 (\d{4})', r'\1 \2', tweetDict['user']['created_at'])

            # Collect the text information.
            if 'extended_tweet' in tweetDict:
                tweet_text = tweetDict['extended_tweet']['full_text']
            elif 'full_text' in tweetDict:
                tweet_text = tweetDict['full_text']
            else:
                tweet_text = tweetDict['text']
            tweet_text = cleaner(tweet_text)
            tweet_text = escape_xml_illegal_chars(tweet_text)

            # Collect response data.
            tweet_favorited = tweetDict['favorite_count']
            tweet_retweeted = tweetDict['retweet_count']

            # Collect hashtags.
            hashtags = tweetDict['entities']['hashtags']  # Added
            if hashtags:
                curr_hashtags = [f'H:{i["text"]}' for i in hashtags]
                hashtag_count = len(curr_hashtags)
                curr_hashtags = (';').join(curr_hashtags)
            else:
                curr_hashtags = ''
                hashtag_count = 0
            # Gather Sentiment Analysis
            sentiment_analysis = round(TextBlob(sentiment_tweet(tweet_text)).polarity, 2)
            subjectivity_analysis = round(TextBlob(sentiment_tweet(tweet_text)).subjectivity, 2)
            iBrk = 0
            # Gather attributes.
            tweet_attributes = f'attr="{curr_hashtags};F:{user_followers};P:{user_posts};f:{tweet_favorited};R:{tweet_retweeted};S:{sentiment_analysis};s:{subjectivity_analysis};h:{hashtag_count}"'
            tweet_attributes = re.sub(r'";', r'"', tweet_attributes)
            tweet_attributes = re.sub(r';"', r'"', tweet_attributes)
            tweet_attributes = re.sub(r';D:;', r';', tweet_attributes)
            tweet_attributes = re.sub(r';l:;', r';', tweet_attributes)

            if user_followers == 0:
                rtf_ratio = 'Invalid'
            else:
                if tweet_retweeted / user_followers != 0:
                    rtf_ratio = round(math.log(tweet_retweeted / user_followers) + 14, 1)
                else:
                    rtf_ratio = 0
                if tweet_favorited / user_followers != 0:
                    ftf_ratio = round(math.log(tweet_favorited / user_followers) + 14, 1)
                else:
                    ftf_ratio = 0
            # Add Tree Structure to WordCruncher Book
            if simple_date not in dateDict:
                dateDict[simple_date] = 1
                my_datetime = datetime.datetime.strptime(simple_date, '%b %d %Y')
                curr_year = my_datetime.year
                curr_month = my_datetime.month
                curr_day = my_datetime.day
                if screen_name not in userDict:
                    userDict[screen_name] = 1
                    refDict = {}
                    print(f'<p><R ref="u,1:{screen_name}"/> </p>', file=etax_file)
                if curr_year not in refDict:
                    refDict[curr_year] = {}
                    print(f'<p><R ref="y,2:{curr_year}"/> </p>', file=etax_file)
                if curr_month not in refDict[curr_year]:
                    refDict[curr_year][curr_month] = []
                    print(f'<p><R ref="m,3:{curr_month}"/> </p>', file=etax_file)
                if curr_day not in refDict[curr_year][curr_month]:
                    refDict[curr_year][curr_month].append(curr_day)
                    print(f'<p just="center"><R ref="d,4:{curr_day}"/> <T st="m">{curr_day} {calendarDict[str(curr_month)]} {curr_year}</T></p>', file=etax_file)

            # Output user information.
            print(f'<p st="user"><R ref="t,5:{tweet_counter}" {tweet_attributes}/><T st="U">{cleaner(name)}</T> <T st="sn">@{cleaner(screen_name)}</T> <T st="m">·</T> <T st="cd">{char_date(creation_date)}</T></p>', file=etax_file)
            # Output tweet information.
            if tweet_text.startswith('RT'):
                print(f'<p st="RT">{tweet_text}</p>', file=etax_file)
            else:
                print(f'<p>{tweet_text}</p>', file=etax_file)

            print(f'<p><T st="m"><b>Retweets</b>:<tab/>{tweet_retweeted}<tab/><b>Favorited</b>:<tab/>{tweet_favorited}<tab/><b>RTF Ratio</b>:<tab/>{rtf_ratio}<tab/><b>FTF Ratio</b>:<tab/>{ftf_ratio}</T></p>', file=etax_file)


print('</etax>', file=etax_file)
print(f'Your tweets have been saved into {etax}!\nPlease use the WordCruncher Publishing Toolkit to convert this into an .etbu file.')

etax_file.close()
