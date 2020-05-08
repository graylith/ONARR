import React, { Component } from 'react'
import axios from 'axios'
import Show from './Show'
class Ndtv extends Component {

  state = {
    data:[]
  }
  componentDidMount(){
      axios.get('http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/ndtv')
      .then(res => {
          this.setState({data:res.data
          });
          console.log(res.data);
      });
  }
  render() {
    return (
      <div>
        <h1>Ndtv</h1>
        <Show data={this.state.data} />        
      </div>
    )
  }
}

export default Ndtv;