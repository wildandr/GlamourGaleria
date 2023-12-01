import React from 'react'
import Banner from '../component/Fashion/Banner'
import BannerBottom from '../component/Fashion/BannerBottom'
import HotProduct from '../component/Fashion/HotProduct'
import Trending from '../component/Fashion/Trending'
import TodayDeal from '../component/Fashion/TodayDeal'
import OfferTime from '../component/Fashion/OfferTime'
import Blog from '../component/Fashion/Blog'
import Footer from '../component/Common/Footer'
import Header from '../component/Common/Header'


const Fashion = () => {
    return (
        <>
            <Header />
            <Banner />
            <BannerBottom />
            <HotProduct />
            <Footer />
        </>
    )
}

export default Fashion