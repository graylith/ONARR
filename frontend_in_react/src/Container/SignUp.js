import React, { Component } from 'react'
import {NavLink} from 'react-router-dom';
import {connect} from 'react-redux';
import * as actions from '../Store/actions/auth';
 class SignUpForm extends Component {
    state = {
        username: "",
        email: "",
        password1: "",
        password2: "",
        errors: {}
      };
    onChangeHandler = event => {
        this.setState({
          [event.target.id]: event.target.value
        });
    };
    handleSubmit = (e) => {
        e.preventDefault();
        this.props.onAuth(
            this.state.username,
            this.state.email,
            this.state.password1,
            this.state.password2,

        );
        
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
                <label htmlFor="username">Username:</label>
                <input type="text" className="form-control" 
                       id="username" value={this.state.username}
                       onChange={this.onChangeHandler}/>
            </div>
            <div className="form-group">
                <label htmlFor="email">Email:</label>
                <input type="email" className="form-control" 
                       id="email" value={this.state.email}
                       onChange={this.onChangeHandler}/>
            </div>
            <div className="form-group">
                <label htmlFor="password">Password:</label>
                <input type="password" className="form-control" 
                    id="password1"  value={this.state.password1}
                    onChange={this.onChangeHandler}/>
            </div>
            
            <div className="form-group">
                <label htmlFor="password2">Confirm Password:</label>
                <input type="password" className="form-control" 
                    id="password2"  value={this.state.password2}
                    onChange={this.onChangeHandler}/>
            </div> 
            <button htmltype="submit" className="btn btn-primary">SignUp</button>
            <NavLink to="/login" style={{margin:"20px"}}>Login</NavLink>
            </form>
        }
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
        onAuth: (username,email,password1,password2) => dispatch(actions.authSignup(username,email,password1,password2)) 
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(SignUpForm);