import React, { useState, useRef } from 'react'
import useSWRMutation from "swr/mutation";
import sendRequest from "./POSTdata";
import Cookies from "js-cookie";
import {useNavigate} from 'react-router-dom';


function Login() {
    const navigate = useNavigate();
    const [getInputLogin, setInputLogin] = useState("")
    const [getInputPassword, setInputPassword] = useState("")

    const handleLoginChange = (e) => {
        setInputLogin(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setInputPassword(e.target.value);
    };

    const [isLoginDialogOpen, setLoginDialogIsOpen] = useState(false);
    const dialogLoginRef = useRef(null);

    const openLoginDialog = () => {
        setLoginDialogIsOpen(true);
        console.log(dialogLoginRef)
        dialogLoginRef.current.showModal();
    };

    const closeLoginDialog = () => {
        setLoginDialogIsOpen(false);
        dialogLoginRef.current.close();
    };

    const {
        trigger
    } = useSWRMutation(`${global.config.urls.baseUrl}/login/`, sendRequest);


    const ConfirmLogin = async () => {
        setLoginDialogIsOpen(false);
        let result = await trigger({login: getInputLogin, password: getInputPassword})

        if (result["token"]) {
            console.log("Token:", result["token"])
            Cookies.set("token", result["token"],
                {
                    expires: 7,
                    path: '/',
                    domain: 'social.vsadmin.ru',
                    secure: false,
                    sameSite: 'none'
                })
            Cookies.set("user_id", result["user_id"])
            navigate('/profile');
            window.location.reload();
        }
        dialogLoginRef.current.close();
    };

    return (
        <div>
            <button className="header_menu_button_signin_signout_register" onClick={openLoginDialog}>SingIn</button>
            <dialog ref={dialogLoginRef} open={isLoginDialogOpen}>
                <div className="edit_post_dialog_wrapper">
                    <div className="edit_post_dialog_header">
                        <p>Login</p>
                    </div>
                    <div className="edit_post_dialog_content">
                        <input value={getInputLogin} onInput={setInputLogin} onChange={handleLoginChange}></input>
                        <input value={getInputPassword} onInput={setInputPassword} onChange={handlePasswordChange}></input>
                    </div>
                    <div className="edit_post_dialog_buttons">
                        <button className="post_menu_button_edit" onClick={ConfirmLogin}>Login</button>
                        <button className="post_menu_button_delete" onClick={closeLoginDialog}>Exit</button>
                    </div>
                </div>
            </dialog>
        </div>
    )
}

export default Login