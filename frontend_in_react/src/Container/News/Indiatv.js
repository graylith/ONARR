import React, { Component } from 'react'
import axios from 'axios'
import Show from './Show'
class indiatv extends Component {

  state = {
    data:[]
  }
  componentDidMount(){
      axios.get('http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/indiatv')
      .then(res => {
          this.setState({data:res.data
          });
          console.log(res.data);
      });
  }
  render() {
    return (
      <div>
        <h1>india TV</h1>
        <Show data={this.state.data} />        
      </div>
    )
  }
}

export default indiatv;