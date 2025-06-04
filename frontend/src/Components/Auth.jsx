import React from "react";
//import useSWRMutation from "swr/mutation";
//import sendRequest from "./POSTdata";


function Auth(props) {
    /*const {
        trigger
    } = useSWRMutation('http://api.vsadmin.ru/login/?login=login&password=password', sendRequest);

    try {
        const newItem = { login: 'log', password: 'pass' };
        const result = trigger(newItem);
        console.log('Item created:', result);
    } catch (error) {
        console.error('Failed to create item:', error);
    }

    return <div></div>
*/
        console.log(props.login, props.pass)
        props.data("ok")
        return <div></div>
    }

export default Auth;