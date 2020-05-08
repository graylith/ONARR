import React from 'react';
import TrendingListView from './TrendingListView';
import CategoryRatioView from './CategoryRatioView';

 const StatsView = (props) => {
    
    return (
      <div>
        <h1>Category Ratio</h1>
         <CategoryRatioView />
         <h1>Trending Keyword</h1>
         <TrendingListView />
       </div>
    )
  }


export default StatsView;