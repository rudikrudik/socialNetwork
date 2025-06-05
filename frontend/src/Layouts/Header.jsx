import React from "react";
import profile_img from "../images/profile/6.jpg"
import {Link} from "react-router-dom";
import Cookies from "js-cookie";


function Header () {
    if (Cookies.get('user_access_token')) {
        return (
            <div className="header">
                <div className="header_wrapper">
                    <div className="header_menu">
                        <p><Link to="/logout">Sing Out</Link></p>
                        <img alt="profile logo" width="5%" src={profile_img}/>
                    </div>
                </div>
            </div>
        )
    } else {
        return (
            <div className="header">
                <div className="header_wrapper">
                    <div className="header_menu">
                        <p><Link to="/register">Join</Link></p>
                        <p><Link to="/login">Sing In</Link></p>
                    </div>
                </div>
            </div>
        )
    }
}

export default Header