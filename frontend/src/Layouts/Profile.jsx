import React from "react";
import profile_img from "../images/profile/6.jpg"
import CreatePost from "./CreatePost";


function Profile () {
    return (
        <div className="main">
            <div className="profile" style={{backgroundImage: `url(${profile_img})`, backgroundSize: 'cover'}}>
                <div className="profile_data">
                    <p>Image</p>
                    <p>Image</p>
                    <p>Image</p>
                </div>
            </div>
            <CreatePost />
        </div>
    )
}

export default Profile;