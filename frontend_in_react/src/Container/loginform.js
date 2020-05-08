import React, { Component } from 'react';
import {NavLink} from 'react-router-dom';
import {connect} from 'react-redux';
import * as actions from '../Store/actions/auth';
 class Loginform extends Component {
    state = {
        id:"",
        username: "",
        password: "",
        errors: {}
      };
    onChangeHandler = event => {
        this.setState({
          [event.target.id]: event.target.value
        });
    };
    handleSubmit = (e) => {
        e.preventDefault();
        this.props.onAuth(this.state.username,this.state.password);
        this.props.history.push('/');
      }
  render() {
    let errorMessage=null;
    if(this.props.error){
        errorMessage=(
            <p>{this.props.error.message}</p>
        );
    }
    return (
        <div className="thumbnail">
        {errorMessage}
        {
            this.props.loading
            ?
                <div className="spinner-border"></div>
            :
            <form onSubmit={this.handleSubmit}>
            <div className="form-group">
                <div className="row">
                    <div className="form-com col-md-4">
                        <label htmlFor="pwd">Username:</label>
                    </div>
                    <div className="form-com col-md-8">
                        <input type="text" className="form-control" id="username" value={this.state.username}
                            onChange={this.onChangeHandler}/>
                    </div>
                </div>
                <div className="row">
                    <div className="form-com col-md-4">
                        <label htmlFor="password">Password:</label>
                    </div>
                    <div className="form-com col-md-8">
                        <input type="password" className="form-control" id="password"  value={this.state.password}
                        onChange={this.onChangeHandler}/>
                    </div>
                </div>
                <div className="row">
                    <div className="form-com col-md-4">
                    <NavLink to="/signup" style={{margin:"20px"}}>SignUp</NavLink>
                    </div>
                    <div className="col-md-8">
                    <button htmltype="form-com submit" className="btn btn-primary">Login</button>
                    </div>
                </div>
                </div>    
                    
               
                
                
                   
            </form>}
        </div>
        
    )
  }
}



const mapStateToProps = (state) =>{
    return {
        loading:state.loading,
        error:state.error
    }

} 
 
const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, password) => dispatch(actions.authLogin(username, password)) 
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(Loginform);