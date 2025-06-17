import React, { useState, useRef } from 'react'
import useSWRMutation from "swr/mutation";
import fetcherPost from "../Components/FetcherPOST";


function CreatePost() {
    const [getInputContent, setInputContent] = useState("")

    const handleChange = (e) => {
        setInputContent(e.target.value);
    };

    const [isEditDialogOpen, setEditDialogIsOpen] = useState(false);
    const dialogEditRef = useRef(null);

    const openEditDialog = () => {
        setEditDialogIsOpen(true);
        dialogEditRef.current.showModal();
    };

    const closeEditDialog = () => {
        setEditDialogIsOpen(false);
        dialogEditRef.current.close();
    };

    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/post/create`],
        ([url]) => fetcherPost(url, {post_content: getInputContent}));


    const ConfirmEdit = async () => {
        setEditDialogIsOpen(false);
        let result = await trigger()
        if (result) {
            window.location.reload();
        }
        dialogEditRef.current.close();
    };

    return (
        <div>
            <button className="create_new_post_button" onClick={openEditDialog}></button>
            <dialog ref={dialogEditRef} open={isEditDialogOpen}>
                <div className="edit_post_dialog_wrapper">
                    <div className="edit_post_dialog_header">
                        <p>Create Post</p>
                    </div>
                    <div className="edit_post_dialog_content">
                        <textarea value={getInputContent} onInput={setInputContent} onChange={handleChange}></textarea>
                    </div>
                    <div className="edit_post_dialog_buttons">
                        <button className="post_menu_button_delete" onClick={closeEditDialog}>Cancel</button>
                        <button className="post_menu_button_edit" onClick={ConfirmEdit}>Save</button>
                    </div>
                </div>
            </dialog>
        </div>
    )
}

export default CreatePost