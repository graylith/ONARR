import React, { Component } from 'react';
import AnchorListView from './AnchorListView';

 class AnchorView extends Component {
    render() {
    return (
      <div>
        
        <AnchorListView {...this.props}></AnchorListView>
    
      </div>
    )
  }
}

export default AnchorView;