import React, { Component } from 'react'
import {Link} from 'react-router-dom'

class Footer extends Component {
  render() {
    return (
    
      <div className="page-footer">
          <footer>
<div className="container">
        <div className="row">
            <div className="col-md-4">
                 <ul> <h4><b>Get to Know Us</b></h4>
                    <h5><Link to="/">About Us</Link></h5>
                    <h5><Link to="/">Contact Us</Link></h5>
                    <h5><Link to="/">Our Team</Link></h5>
               </ul>
            </div>
            <div className="col-md-4">
                    <ul><h4><b>Follow US</b></h4>
                    <h5><Link to="/"> Facebook</Link></h5>
                        <h5><Link to="/">Twitter</Link></h5>
                    <h5><Link to="/">Instagram</Link></h5>
                </ul>
            </div>
            <div className="col-md-4">
                <ul><h4><b>Useful Links</b></h4>
                    <h5><Link to="/login"> Login</Link></h5>
                    <h5><Link to="/signup"> SignUp</Link></h5>
                    <h5><Link to="/">Report</Link></h5>
                    <h5><Link to="/">Logout</Link></h5>


                </ul>
            </div>
        </div>
        <div className="row">
            <div className="col-md-3">

            </div>
            <div className="col-md-6">
                <p style={{textAlign:"center"}}>©2019, Save4thPillar </p>
            </div>
            <div className="col-md-3">

            </div>
        </div>

</div>
</footer>       
      </div>
      
      
    )
  }
}

export default Footer;
