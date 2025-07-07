import Cookies from "js-cookie";
import {useNavigate} from "react-router-dom";
import React from "react";

function Logout () {
    const navigate = useNavigate();


    const logoutButton = () => {
        Cookies.remove('token');
        Cookies.remove('user_id');
        window.location.reload();
        navigate('/login');
    }

    return (
        <div>
            <button className="header_menu_button_signin" onClick={logoutButton}>SingOut</button>
        </div>
    )
}

export default Logout