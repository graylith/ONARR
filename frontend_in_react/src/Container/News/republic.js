import React, { Component } from 'react'
import axios from 'axios'
import Show from './Show'
class Republic extends Component {

  state = {
    data:[]
  }
  componentDidMount(){
      console.log("Hello");
      axios.get('http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/republic')
      .then(res => {
          this.setState({data:res.data
          });
          console.log(res.data);
      });
  }
  render() {
    return (
      <div>
        <h1>Republic</h1>
        <Show data={this.state.data} />        
      </div>
    )
  }
}

export default Republic;