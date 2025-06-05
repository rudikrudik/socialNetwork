import React, {useState} from "react";
import profile_img from "../images/profile/6.jpg"
import sendRequest from "../Components/POSTdata";
import useSWRMutation from "swr/mutation";
import Cookies from 'js-cookie';
import {useNavigate} from 'react-router-dom';
import '../config';


function Login () {
    const [loginInput, setLoginInput] = useState("")
    const [passwordInput, setPasswordInput] = useState("")
    const navigate = useNavigate();

    const handleInputLogin = (event) => {
        setLoginInput(event.target.value);
    };

    const handleInputPassword = (event) => {
        setPasswordInput(event.target.value);
    };

    const {
        trigger
    } = useSWRMutation(`${global.config.urls.baseUrl}/login/`, sendRequest);

    const handlerClick = async () => {
        try {
            let result = await trigger({login: loginInput, password: passwordInput})

            if (result["token"]) {
                Cookies.set('user_access_token', result["token"],
                    {
                        secure: true,
                        sameSite: "Strict",
                        expires: 7
                    });
                navigate('/');
                    }
            }
        catch (e) {
                // error handling
            }
        }

return (
<div className="main">
    <div className="profile" style={{backgroundImage: `url(${profile_img})`, backgroundSize: 'cover'}}>
        <div className="profile_data">
            <input type="text" value={loginInput} onChange={handleInputLogin}/>
            <input type="text" value={passwordInput} onChange={handleInputPassword}/>
                <button onClick={handlerClick}>Login</button>
        </div>
    </div>
</div>
)
}

export default Login;