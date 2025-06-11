import React, { useState, useRef } from 'react'
import useSWRMutation from "swr/mutation";
import fetcherPost from "../Components/FetcherPOST";


function DeletePost(props) {
    const id_post = {id: props.id_post};
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

    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/post/delete`, id_post],
        ([url, id_post]) => fetcherPost(url, id_post));


    const ConfirmDelete = async () => {
        setDeleteDialogIsOpen(false);
        let result = await trigger()
        if (result){
            window.location.reload();
        }
        dialogRef.current.close();
    };

    return (
        <div>
            <button className="post_menu_button_delete" onClick={openDeleteDialog}>Delete</button>
                <dialog ref={dialogRef} open={isDeleteDialogOpen}>
                    <h2>Confirm Delete?</h2>
                        <button className="post_menu_button_edit" onClick={closeDeleteDialog}>Cancel</button>
                        <button className="post_menu_button_delete" onClick={ConfirmDelete}>Confirm</button>
                </dialog>
        </div>
    )
}

export default DeletePost