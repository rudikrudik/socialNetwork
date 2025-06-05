import React, {useState} from "react";


function Auth(props) {
    console.log("In auth")
    console.log(props.data)
    props.token(props.data)
}

export default Auth;