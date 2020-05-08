import React, { Component } from 'react';
import Ndtv from './ndtv';
import Hindustan from './Hindustan';
import Indianexpress from './Indianexpress';
import Indiatv from './Indiatv';
import News18 from './News18';
import Oneindia from './Oneindia';
import Republic from './republic';
import Thehindu from './Thehindu';
import Zeenews from './Zeenews';
import Firstpost from './Firstpost';
import {Link,Route,BrowserRouter} from 'react-router-dom';


class NewsListView extends Component {
    render() {
    return (
      <div>
        <h1>News</h1>
        <BrowserRouter>
        <ul className="nav nav-tabs">
          <table>
            <tbody>
              <tr>
                <td>
                  <li className="tab-link"><Link  to="/ndtv-news">Ndtv</Link></li>
                </td>
                <td>
                <li className="tab-link"><Link  to="/republic-news">Republic</Link></li>
                </td>
                <td>

              <li className="tab-link"><Link  to="/zeenews-news">Zee News</Link></li>
                </td>
                <td>

              <li className="tab-link"><Link  to="/firstpost">Firstpost</Link></li>
                </td>
                <td>
                <li className="tab-link"><Link  to="/indianexpress-news">Indian Express</Link></li>
                </td>
                <td>
                <li className="tab-link"><Link  to="/indiatv-news">India TV</Link></li>
                </td>
                <td>
                <td>
                <li className="tab-link"><Link  to="/News18-news">News18</Link></li>
                </td>                </td>
                <td>
                <li className="tab-link"><Link  to="/oneindia-news">One India</Link></li>
                </td>
                <td>
                <li className="tab-link"><Link  to="/Thehindu-news">The Hindu</Link></li>
                </td>
                                
              </tr>
              </tbody>
          </table>
             
              
          </ul>
          <div className="tab-content">
              <Route exact path="/ndtv-news" component={Ndtv} />
              <Route exact path="/republic-news" component={Republic} />
              <Route exact path="/zeenews-news" component={ Zeenews } />
              <Route exact path="/hindustan-news" component={Hindustan} />
              <Route exact path="/indianexpress-news" component={Indianexpress} />
              <Route exact path="/indiatv-news" component={ Indiatv } />
              <Route exact path="/news18-news" component={News18} />
              <Route exact path="/oneindia-news" component={Oneindia} />
              <Route exact path="/thehindu-news" component={ Thehindu } />
              <Route exact path="/firstpost" component={Firstpost} />
            </div> 
          </BrowserRouter>
    
      </div>
    )
  }
}

export default NewsListView;