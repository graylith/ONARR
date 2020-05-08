import React, { Component } from 'react'
import SingleHeadLine from './SingleHeadLine'
class NewsSource extends Component {
  render() {
      if (this.props && this.props.data) {
        var oneNewsCard =
          this.props &&
          this.props.data &&
          this.props.data[1].map((item, index) => {
            return (
                <SingleHeadLine
                  key={index}
                  data={item}
                  source={this.props.data[0]}
                />
            );
          });
      } else return null;

    return (
      <div>
      let source={this.props.data[0]};
      <h1 style={{textAlign: "center"}}>{this.props.data[0]}</h1>
      <hr></hr>
        {oneNewsCard}
        
      </div>
    )
  }
}

export default NewsSource;
