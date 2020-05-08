import React, { Component } from 'react';
import Header from './Components/header';
import {BrowserRouter} from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from './Store/actions/auth';

import './app.css';
import './bootstrap.min.css';
class App extends Component {

  componentDidMount() {
    this.props.onTryAutoSignup();

  }

  render() {
    return (
      <div>
      <BrowserRouter>
        <div>
          <Header {...this.props}>
          </Header>
        </div>
      </BrowserRouter>
      </div>
    )
  }
}

const mapStateToProps = state => {
  return {
    isAuthenticated: state.token !== null
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onTryAutoSignup: () => dispatch(actions.authCheckState())
  }
}
export default connect(mapStateToProps, mapDispatchToProps)(App);
  

