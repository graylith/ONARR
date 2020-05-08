import React, { Component } from 'react'
import axios from 'axios'
import SearchNews from './SearchNews'

class keywordNews extends Component {
  state = {
      data:{}
    }
    componentDidMount(){
        const keyword=localStorage.getItem('keyword');
        const url=`http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/news/${keyword}`;
        axios.get(url)
        .then(res => {
          this.setState({data:res.data
          });
          console.log(res.data);
      });
    }
render() {
  return (
    <div>
      <div  className="local-storage-keyword">
        Category : #{localStorage.getItem('keyword')}
      </div>
      <br/>
      <SearchNews data={this.state.data} /> 
    </div>
  )
}
}
export default keywordNews;