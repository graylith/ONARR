
import React, { Component } from 'react'
import {Link} from 'react-router-dom'

class SingleHeadLine extends Component {
  render() {
    return (
      <div style={{margin: "10px 40px", background: "#eee", padding: "1px 10px", borderRadius: "10px"}}>
        <Link to={this.props.data.link}>{this.props.data.headline}</Link>
        <h6>{this.props.data.date}</h6>
      </div>
    )
  }
}

export default SingleHeadLine;