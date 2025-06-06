import React, { useState, useRef } from 'react'
import profile_img from "../images/profile/6.jpg"
import Cookies from "js-cookie";
import useSWR from "swr";
import fetch_with_args from "../Components/FetcherWIthAuth";
import useSWRMutation from "swr/mutation";
import fetcher_cookie from "../Components/FetcherCookie";

function Posts(props) {
    const date = new Date(Date.parse(props.data[2].toString()));
    const formattedDate = new Intl.DateTimeFormat('en-US', {
        hour12: false,
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(date);

    const [isOpen, setIsOpen] = useState(false);
    const dialogRef = useRef(null);


    const openDialog = () => {
        setIsOpen(true);
        dialogRef.current.showModal();
    };

    const closeDialog = () => {
        setIsOpen(false);
        dialogRef.current.close();
    };

    const token = Cookies.get('user_access_token');
    const id = props.data[0];

    const headers = {
        method: 'POST',
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        Cookies: `user_access_token=${token}`,
        'Content-Type': 'application/json',
    };


    const requestOptions = {
        method: 'POST',
        headers: {
            'Access-Control-Allow-Origin': 'http://localhostdata:3000',
            Cookies: `user_access_token=${token}`,
            'Content-Type': 'application/json'},
        body: JSON.stringify({id: props.data[0]})
    };


    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/post/delete`, requestOptions],
        ([url, requestOptions]) => fetch_with_args(url, requestOptions));


    const ConfirmDelete = async () => {
        setIsOpen(false);
        console.log("Before Delete", props.data[0])
        let result = await trigger({id: props.data[0]})
        console.log("After Delete result", result)
        dialogRef.current.close();
    };


    return (
        <div className="post">
            <div className="post_author_menu_wrapper">
                <div className="post_author">
                    <img alt="profile logo" src={profile_img}/>
                    <p>Виталий Солохов</p>
                </div>
                <div className="post_post_date">
                    <p>{formattedDate}</p>
                </div>
            </div>
            <div className="post_content_menu">
                <p>{props.data[3]}</p>
            </div>
            <div className="post_edit_menu_wrapper">
                <div className="post_edit_menu">
                    <button className="post_menu_button_edit">Edit</button>
                    <button className="post_menu_button_delete" onClick={openDialog}>Delete</button>
                    <dialog ref={dialogRef} open={isOpen}>
                        <h2>Dialog Title</h2>
                        <p>This is the content of the dialog.</p>
                        <button onClick={closeDialog}>Cancel</button>
                        <button onClick={ConfirmDelete}>Delete</button>
                    </dialog>
                </div>
            </div>
        </div>
    )
}

export default Posts