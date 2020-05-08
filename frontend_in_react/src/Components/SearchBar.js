import React, { Component } from 'react'

class SearchBar extends Component {
  state={term:''};
  onInputChange = event =>{
      this.setState({term:event.target.value});
  }; 

  onFormSubmit = event => {
      event.preventDefault();
      this.props.onFormSubmit(this.state.term); 
  };
  render() {
    return (
      <div>
        <div className="thumbnail-center">
            <p>Search News From All Sources</p>
      
             <div id="search-bar">
                <form onSubmit={this.onFormSubmit } >
                    <input type="text" value={this.state.value}
                    onChange={this.onInputChange}/>
                </form>
                
             </div>
      </div>
</div>
   
      
    )
  }
}

export default SearchBar;