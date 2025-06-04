import React from "react";
import profile_img from "../images/profile/6.jpg"
import {Link} from "react-router-dom";

function Header () {
    return (
        <div className="header">
            <div className="header_wrapper">
                <div className="header_menu">
                    <p>Register</p>
                    <Link to="/login" ><p>Login</p></Link>
                    <img alt="profile logo" width="5%" src={profile_img}/>
                </div>
            </div>
        </div>
    )
}

export default Header