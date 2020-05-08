import React, { Component } from 'react';
class SearchNews extends Component {
  RenderData = () => {
    const { data } = this.props;
    return Object.keys(data).map((key) => {
      return (
        <div key={key}>
        { data[key].map(({headline, date, link,category}, index) => {
          return (
            <div className="Newscards" key={index}>
              <div className="row">
                <div className="col-md-12">
                  <a href={link}>{headline} </a>
                </div>
              </div>
              <div className="row">
                <div className="col-md-3">
                </div>
                <div className="col-md-9">
                <div className="col-md-4 align-div-right">
                  Date: {date.substring(0, 11)} 
                </div>
                <div className="col-md-4 align-div-center">
                  {category} 
                </div>
              <div className="col-md-4 align-div-left">
                  Source:<b>{key}</b>
              </div>
                
                </div>
              </div>
              <h4></h4>
            </div>
          )
        })}


          <br/>
          <br />
        </div>
      )
    }
    );
  }

  render() {
    const { RenderData } = this;
    const { data } = this.props;

    return (
      <div>
        {data && <RenderData />}
       </div>
    )
  }
}

export default SearchNews;