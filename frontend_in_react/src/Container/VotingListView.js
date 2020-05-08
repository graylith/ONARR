import React from 'react';
import axios from 'axios';
import Voting from '../Components/Voting';


class TrendingList extends React.Component{
  state = {
    data:[],
    
  }

  componentDidMount(){
    axios.get('http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/')
    .then(res => { 
        this.setState({data: res.data});
    })
    
  }
  render(){
      return (
        <Voting data={this.state.data} ></Voting>
        )
  }
}

export default TrendingList;