import React, {useState} from "react";
import profile_img from "../images/profile/6.jpg"
import useSWRMutation from "swr/mutation";
import sendRequest from "../Components/POSTdata";


function Login () {
    const [loginInput, setLoginInput] = useState("")
    const [passwordInput, setPasswordInput] = useState("")
    const [token, setToken] = useState("error");

    let result = ""

    const handleInputLogin = (event) => {
        setLoginInput(event.target.value);
    };

    const handleInputPassword = (event) => {
        setPasswordInput(event.target.value);
    };

    const {
        trigger
    } = useSWRMutation('http://api.vsadmin.ru/login/', sendRequest);

return (
<div className="main">
    <div className="profile" style={{backgroundImage: `url(${profile_img})`, backgroundSize: 'cover'}}>
        <div className="profile_data">
            <input type="text" value={loginInput} onChange={handleInputLogin}/>
            <input type="text" value={passwordInput} onChange={handleInputPassword}/>
                <button
                    onClick={async () => {
                        try {
                            result  = await trigger({ login: loginInput, password: passwordInput})
                            console.log(result)
                            //setToken(result["detail"])
                        } catch (e) {
                            // error handling
                        }
                    }}
                >Login</button>
            <p>Login status: {token}</p>
        </div>
    </div>
</div>
)
}

export default Login;