import React, { Component } from 'react'
import axios from 'axios'
import Show from './Show'
class News18 extends Component {

  state = {
    data:[]
  }
  componentDidMount(){
      axios.get('http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/news18')
      .then(res => {
          this.setState({data:res.data
          });
          console.log(res.data);
      });
  }
  render() {
    return (
      <div>
        <h1>News18</h1>
        <Show data={this.state.data} />        
      </div>
    )
  }
}

export default News18;