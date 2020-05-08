import React, { Component } from 'react';
import VotingListView from './VotingListView';

 class VotingView extends Component {
    render() {
    return (
      <div>
        
        <VotingListView {...this.props}></VotingListView>
    
      </div>
    )
  }
}

export default VotingView;