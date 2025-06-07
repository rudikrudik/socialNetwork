import React, { useState, useRef } from 'react'
import profile_img from "../images/profile/6.jpg"
import useSWRMutation from "swr/mutation";
import fetcherPost from "../Components/FetcherPOST";
import {useNavigate} from "react-router-dom";

function Posts(props) {
    const navigate = useNavigate();

    const date = new Date(Date.parse(props.data[2].toString()));
    const formattedDate = new Intl.DateTimeFormat('en-US', {
        hour12: false,
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(date);

    const [isDeleteDialogOpen, setDeleteDialogIsOpen] = useState(false);
    const dialogRef = useRef(null);


    const openDeleteDialog = () => {
        setDeleteDialogIsOpen(true);
        dialogRef.current.showModal();
    };

    const closeDeleteDialog = () => {
        setDeleteDialogIsOpen(false);
        dialogRef.current.close();
    };

    const id_post = {id: props.data[0]};

    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/post/delete`, id_post],
        ([url, id_post]) => fetcherPost(url, id_post));


    const ConfirmDelete = async () => {
        setDeleteDialogIsOpen(false);
        let result = await trigger()
        if (result){
            return navigate('/user/posts');
        }
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
                    <button className="post_menu_button_delete" onClick={openDeleteDialog}>Delete</button>
                    <dialog ref={dialogRef} open={isDeleteDialogOpen}>
                        <h2>Dialog Title</h2>
                        <p>This is the content of the dialog.</p>
                        <button onClick={closeDeleteDialog}>Cancel</button>
                        <button onClick={ConfirmDelete}>Delete</button>
                    </dialog>
                </div>
            </div>
        </div>
    )
}

export default Posts