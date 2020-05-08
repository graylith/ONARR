import React, { Component } from 'react'
import axios from 'axios'
import SearchNews from './SearchNews'

class keywordNews extends Component {
  state = {
      data:{}
    }
    componentDidMount(){
        const keyword=localStorage.getItem('keyword');
        const url=`http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/keyword/${keyword}`;
        console.log(url);
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
        Search Result for : #{localStorage.getItem('keyword')}
      </div>
      <br/>
      <SearchNews data={this.state.data} /> 
    </div>
  )
}
}
export default keywordNews;