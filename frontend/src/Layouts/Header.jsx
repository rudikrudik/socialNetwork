import React from "react";
import profile_img from "../images/profile/6.jpg"
import {Link} from "react-router-dom";
import Cookies from "js-cookie";
import Login from "../Components/Login";
import Logout from "../Components/Logout";
import Register from "../Components/Register";


function Header (props) {
    if (Cookies.get('token')) {
        return (
            <div className="header">
                <div className="header_wrapper">
                    <div className="header_menu">
                        <Logout />
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
                        <Register />
                        <Login/>
                    </div>
                </div>
            </div>
        )
    }
}

export default Header