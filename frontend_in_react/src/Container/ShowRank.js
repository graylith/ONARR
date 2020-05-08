import React, { Component } from 'react';


 class ShowRank extends Component {
    
  render() {
    return (
        <div>
            <div>
            
                <div>
                <table className="rank-table table-striped table table-responsive">
                <div  className="rank-headline">
                Rank based on User Voting
            </div>
                {this.props.data.map(({name }, index) => 
                    <div key={index}>
                            <tr><td>{index+1}</td><td>{name}</td></tr>
                    </div>
                 )}
                   </table>
                </div>
              
        </div>
       </div>
    )
  }
}

export default ShowRank;