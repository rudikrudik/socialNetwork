import React from "react";
import profile_img from "../images/profile/6.jpg"
import CreatePost from "./NewPostMenu";
import Posts from "./Posts";
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Cookies from "js-cookie";


function Profile () {
    const user_id = Cookies.get("user_id");

    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/user/get/?id_user=${user_id}`],
        ([url]) => fetcherGet(url));

    if (isLoading) return <div>is Loading</div>;
    if (error) return <div>Error</div>;

    return (
        <div className="main">
            <div className="profile" style={{backgroundImage: `url(${profile_img})`, backgroundSize: 'cover'}}>
                <div className="profile_data">
                    <p>{data.first_name} {data.last_name}</p>
                </div>
            </div>
            <CreatePost />
            <Posts user={data}/>
        </div>
    )
}

export default Profile;