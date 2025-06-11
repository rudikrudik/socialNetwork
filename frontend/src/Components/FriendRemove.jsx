import React from 'react'
import useSWRMutation from "swr/mutation";
import fetcherPost from "../Components/FetcherPUT";


function FriendRemove(props) {
    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/friends/delete?friend_id=${props.friend_id}`],
        ([url]) => fetcherPost(url));


    const addFriend = async () => {
        let result = await trigger()
        console.log("Delete Result", result)
        if (!result) {
            window.location.reload();
        }
    };

    return (
        <div>
            <button className="post_menu_button_delete" onClick={addFriend}>Remove</button>
        </div>
    )
}

export default FriendRemove