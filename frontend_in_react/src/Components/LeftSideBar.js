import React, { Component } from 'react'
import axios from 'axios';
import ShowRank from '../Container/ShowRank'
class LeftSideBar extends Component {
    state = {
        data:[]
      }
      componentDidMount(){
          axios.get('http://127.0.0.1:8000/api/rankchannel')
          .then(res => {
              this.setState({data:res.data
              });
          });
          console.log("from right side "+this.state.data);
      }
    render() {
        return (
            <div>
                
               <ShowRank data={this.state.data} />     
                
            </div>
        )
    }
}

export default LeftSideBar;
