import React from "react";
import profile_img from "../images/profile/6.jpg"
import FriendAdd from "../Components/FriendAdd";


function SearchFriendsPage(props) {
    return (
        <div className="friend">
            <div className="friend_wrapper">
                <div className="friend_author">
                    <img alt="avatar" src={profile_img} />
                    <p>{props.data[1]} {props.data[2]}</p>
                </div>
                <div className="friend_edit_menu">
                    <FriendAdd friend_id={props.data[0]}/>
                </div>
            </div>
        </div>
    )
}

export default SearchFriendsPage;