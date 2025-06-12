import React from "react";
import profile_img from "../images/profile/6.jpg"
import CreatePost from "./CreatePost";
import Posts from "./Posts";
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";


function Profile () {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/user/posts/`],
        ([url]) => fetcherGet(url));


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
            <Posts />
        </div>
    )
}

export default Profile;