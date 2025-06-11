import React from 'react'
import useSWRMutation from "swr/mutation";
import fetcherPUT from "../Components/FetcherPUT";


function FriendAdd(props) {

    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/friends/set?friend_id=${props.friend_id}`],
        ([url]) => fetcherPUT(url));


    const addFriend = async () => {
        let result = await trigger()
        console.log(result)
        if (result) {
            window.location.reload();
        }
    };

    return (
        <div>
            <button className="post_menu_button_edit" onClick={addFriend}>Add</button>
        </div>
    )
}

export default FriendAdd