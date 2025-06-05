import Cookies from "js-cookie";
import {useNavigate} from "react-router-dom";
import React from "react";

function Logout () {
    const navigate = useNavigate();

    Cookies.remove('user_access_token');
    navigate('/login');

    return (
        <div className="main">
            <div className="profile">
                <div className="profile_data">
                    <p>Goodbye</p>
                </div>
            </div>
        </div>
    )
}

export default Logout