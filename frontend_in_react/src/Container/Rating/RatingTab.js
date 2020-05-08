import React, { Component } from 'react';
import {Link,Route,BrowserRouter} from 'react-router-dom';
import VotingView from '../VotingView';
import AnchorView from './AnchorView'

class RatingTab extends Component {
    render() {
    return (
      <div>
        <h1>Rating</h1>
        <BrowserRouter>
        <ul className="nav nav-tabs">
          <table>
            <tbody>
              <tr>
                <td>
                  <li className="tab-link"><Link  to="/">News Channel</Link></li>
                </td>
                <td>
                  <li className="tab-link"><Link  to="/rate-anchor">News Anchor</Link></li>
                </td>
              </tr>
              </tbody>
          </table>
             
              
          </ul>
          <div className="tab-content">
              <Route exact path="/" component={VotingView}  />
              <Route exact path="/rate-anchor" component={AnchorView} />
            </div> 
          </BrowserRouter>
    
      </div>
    )
  }
}

export default RatingTab;