import React from "react";
import useSWR from "swr";
import Cookies from "js-cookie";
import fetcher_cookie from "../Components/FetcherCookie";
import '../config';

function Posts () {
    const token = Cookies.get('user_access_token');

    const headers = {
        user_access_token: token,
        'Content-Type': 'application/json'
    };
    const {
        data
    } = useSWR([`${global.config.urls.baseUrl}/user/posts`, headers], ([url, headers]) => fetcher_cookie(url, headers));


    console.log("Data", data)

    return (
        <div className="main">
            <div className="posts">
                <div className="profile_data">
                    <p>Posts</p>
                </div>
            </div>
        </div>
    )
}

export default Posts