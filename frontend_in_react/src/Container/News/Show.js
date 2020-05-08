import React, { Component } from 'react';


 class Show extends Component {
    
  render() {
    return (
        <div>
            <div>
                {this.props.data.map(({headline,link,date,category }, index) => 
                    <div key={index}>
                        <div className="Newscards">
              <div className="row">
                <div className="col-md-12">
                  <a href={link}>{headline} </a>
                </div>
              </div>
              <div className="row">
                <div className="col-md-4">
                </div>
                <div className="col-md-8">
                    <div className="col-md-6 align-div-right">
                    Date: {date.substring(0,10)} 
                    </div>
                    <div className="col-md-6 align-div-left">
                        <b>{category}</b>
                    </div>
                </div>
              </div>
              <h4></h4>
            </div>
                    </div>
                 )}
              
        </div>  
       
           <br></br>
       </div>
    )
  }
}

export default Show;