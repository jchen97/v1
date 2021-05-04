import multiprocessing

import fdatable
import rss_feed, rss_feed_2, cnbc, nytimes, currentev, theinfo, verge, trac, citron, hindenburg, scorpion, pacer_feed
import ticker_finder
import headline_filter
import requests
import datetime

if __name__ == '__main__':

    ticker_finder.initiate()
    headline_filter.initiate()
    cnbc.fill()

    session1 = requests.Session()
    session2 = requests.Session()

    runthru = 0

    while True:

        # cnbc
        # cnbcMainx = multiprocessing.Process(target=cnbc.cnbcMain())
        # cnbcUSx = multiprocessing.Process(target=cnbc.cnbcUS())
        # cnbcEUx = multiprocessing.Process(target=cnbc.cnbcEU())
        # cnbcASx = multiprocessing.Process(target=cnbc.cnbcAS())

        # key rss
        ftcprlx = multiprocessing.Process(target=rss_feed.ftcprl())
        nypmainx = multiprocessing.Process(target=rss_feed.nypmain())
        # fdaprlx = multiprocessing.Process(target=rss_feed.fdaprl())
        # ptabx = multiprocessing.Process(target=rss_feed_2.ptab())
        # itc1x = multiprocessing.Process(target=rss_feed_2.itc1())
        uspsx = multiprocessing.Process(target=rss_feed_2.uspsnewsroom())
        applex = multiprocessing.Process(target=rss_feed_2.applenewsroom())




        # influential tech sites
        # theinfox = multiprocessing.Process(target=theinfo.info())
        # info_articlesx = multiprocessing.Process(target=theinfo.info_articles())
        # cnetNewsx = multiprocessing.Process(target=rss_feed_2.cnetNews())

        # vergex = multiprocessing.Process(target=verge.verge())
        # ^too slow now! tweety faster
        # techcrunchx = multiprocessing.Process(target=rss_feed.techcrunch())
        insideevx = multiprocessing.Process(target=rss_feed.insideev())

        citronx = multiprocessing.Process(target=citron.citron(session1))
        # hindenburgx = multiprocessing.Process(target=hindenburg.hindenburg())
        zerotvx = multiprocessing.Process(target=rss_feed.zerotv())
        # scorpionx = multiprocessing.Process(target=scorpion.scorpion())

        # health
        # cnnhealth = multiprocessing.Process(target=rss_feed_2.cnnhealth())
        feuersteinx = multiprocessing.Process(target=rss_feed_2.feuerstein())
        statnewsx = multiprocessing.Process(target=rss_feed_2.statnews())
        # fdatablex = multiprocessing.Process(target=fdatable.fdaTable())

        # nyt
        # nytusx = multiprocessing.Process(target=nytimes.nytus())
        # nyttechx = multiprocessing.Process(target=nytimes.nyttech())
        # nytbusx = multiprocessing.Process(target=nytimes.nytbus())

        # cdcx = multiprocessing.Process(target=currentev.cdc())

        # multichannelx = multiprocessing.Process(target=currentev.multichannel())

        # TRAC
        # tracScrapex = multiprocessing.Process(target=trac.tracScrape())

        # Pacer
        # courtAx = multiprocessing.Process(target=pacer_feed.courtA())
        # courtBx = multiprocessing.Process(target=pacer_feed.courtB())


        ##########################################################

        # tracScrapex.start()

        # cnbcUSx.start()
        # cnbcMainx.start()
        # cnbcEUx.start()
        # cnbcASx.start()

        #fdaprlx.start()
        ftcprlx.start()
        nypmainx.start()
        # ptabx.start()
        # itc1x.start()
        uspsx.start()
        applex.start()


        # cdcx.start()
        # cnnhealth.start()
        feuersteinx.start()
        statnewsx.start()
        # fdatablex.start()

        # vergex.start()
        # theinfox.start()
        # info_articlesx.start()
        # cnetNewsx.start()
        # techcrunchx.start()
        insideevx.start()

        citronx.start()
        #if runthru % 10 == 0:
            # hindenburgx.start()
        zerotvx.start()
        # scorpionx.start()

        # nytusx.start()
        # nytbusx.start()
        # nyttechx.start()

        # multichannelx.start()

        # courtAx.start()
        # courtBx.start()

        runthru = runthru + 1

