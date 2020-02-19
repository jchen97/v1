import multiprocessing
import rss_feed, rss_feed_2, cnbc, nytimes, currentev, theinfo, verge
import ticker_finder
import headline_filter


if __name__ == '__main__':

    ticker_finder.initiate()
    headline_filter.initiate()
    # cnbc.fill()

    while True:


        # cnbc
        cnbcMainx = multiprocessing.Process(target=cnbc.cnbcMain())
        cnbcUSx = multiprocessing.Process(target=cnbc.cnbcUS())
        cnbcEUx = multiprocessing.Process(target=cnbc.cnbcEU())
        cnbcASx = multiprocessing.Process(target=cnbc.cnbcAS())

        # key rss
        ftcprlx = multiprocessing.Process(target=rss_feed.ftcprl())
        nypmainx = multiprocessing.Process(target=rss_feed.nypmain())
        citronx = multiprocessing.Process(target=rss_feed.citron())
        fdaprlx = multiprocessing.Process(target=rss_feed.fdaprl())
        ptabx = multiprocessing.Process(target=rss_feed_2.ptab())

        # influential tech sites
        vergex = multiprocessing.Process(target=verge.verge())
        # theinfox = multiprocessing.Process(target=theinfo.info())
        cnetNewsx = multiprocessing.Process(target=rss_feed_2.cnetNews())

        # health
        cnnhealth = multiprocessing.Process(target=rss_feed_2.cnnhealth())
        feuersteinx = multiprocessing.Process(target=rss_feed_2.feuerstein())

        # nyt
        nytusx = multiprocessing.Process(target=nytimes.nytus())
        nyttechx = multiprocessing.Process(target=nytimes.nyttech())
        nytbusx = multiprocessing.Process(target=nytimes.nytbus())

        # cdcx = multiprocessing.Process(target=currentev.cdc())

        multichannelx = multiprocessing.Process(target=currentev.multichannel())

        ##########################################################

        cnbcUSx.start()
        cnbcMainx.start()
        cnbcEUx.start()
        cnbcASx.start()

        fdaprlx.start()
        ftcprlx.start()
        nypmainx.start()
        citronx.start()
        ptabx.start()



        # cdcx.start()
        cnnhealth.start()
        feuersteinx.start()

        vergex.start()
        # theinfox.start()
        cnetNewsx.start()

        nytusx.start()
        nytbusx.start()
        nyttechx.start()

        multichannelx.start()
