import React, { Component } from 'react';
import {Link} from 'react-router-dom';

 class NewsPage extends Component {
    
  render() {
    return (
        <div>
            <div>
                {this.props.data.map(({headline,link,date }, index) => 
                    <div key={index}>
                        <div>
                            <h3><a href={link}>{headline}</a></h3> 
                            <h6>{date}</h6>           
                        </div>
                    </div>
                 )}
              
        </div>  
       
           <br></br>
           
          
   
       </div>
    )
  }
}

export default NewsPage;