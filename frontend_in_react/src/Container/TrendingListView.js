import React from 'react';
import Trending from '../Components/Trending'
import axios from 'axios';


class TrendingList extends React.Component{
  
  state = {
    data:[],
    frequency: [],
    keyword: []
  }

  componentDidMount(){
    axios.get('http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/trending')
    .then(res => {
      const data = res.data;
      data.map(d => {
        this.state.keyword.push(d.db_keyword)
        this.state.frequency.push(d.db_frequency);
      })
      this.setState({
        data: res.data
              });
    }) 
  }
  render(){
      return (
        <Trending keyword={this.state.keyword} frequency={this.state.frequency}/>
      )
  }
}

export default TrendingList;