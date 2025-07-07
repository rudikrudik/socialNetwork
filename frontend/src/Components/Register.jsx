import React, { useState, useRef } from 'react'
import useSWRMutation from "swr/mutation";
import sendRequest from "./POSTdata";
import {useNavigate} from 'react-router-dom';


function Register() {
    const navigate = useNavigate();
    const [getInputLogin, setInputLogin] = useState("")
    const [getInputPassword, setInputPassword] = useState("")
    const [getInputFirstName, setInputFirstName] = useState("")
    const [getInputLastName, setInputLastName] = useState("")

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
    } = useSWRMutation(`${global.config.urls.baseUrl}/user/register/`, sendRequest);


    const ConfirmLogin = async () => {
        setLoginDialogIsOpen(false);
        let result = await trigger({login: getInputLogin,
                                    password: getInputPassword,
                                    first_name: getInputFirstName,
                                    last_name: getInputLastName})
        navigate('/login')
        dialogLoginRef.current.close();
    };

    return (
        <div>
            <button className="header_menu_button_signin" onClick={openLoginDialog}>Register</button>
            <dialog ref={dialogLoginRef} open={isLoginDialogOpen}>
                <div className="edit_post_dialog_wrapper">
                    <div className="edit_post_dialog_header">
                        <p>Register</p>
                    </div>
                    <div className="edit_post_dialog_content">
                        <input value={getInputLogin} onInput={setInputLogin} onChange={handleLoginChange}></input>
                        <input value={getInputPassword} onInput={setInputPassword} onChange={handlePasswordChange}></input>
                    </div>
                    <div className="edit_post_dialog_buttons">
                        <button className="post_menu_button_edit" onClick={ConfirmLogin}>Register</button>
                        <button className="post_menu_button_delete" onClick={closeLoginDialog}>Exit</button>
                    </div>
                </div>
            </dialog>
        </div>
    )
}

export default Register