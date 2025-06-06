import React from "react";
import useSWR from "swr";
import Cookies from "js-cookie";
import fetcher_cookie from "../Components/FetcherCookie";
import '../config';

function Posts () {
    const token = Cookies.get('user_access_token');

    const headers = {
        mode: "cors",
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        Cookies: `user_access_token=${token}`,
        'Content-Type': 'application/json'
    };
    const {
        data
    } = useSWR([`${global.config.urls.baseUrl}/user/posts`, headers], ([url, headers]) => fetcher_cookie(url, headers));

    console.log("data ", data)

    return (
        <div className="main">
            <div className="posts">
                <p>Posts</p>
            </div>
        </div>
    )
}

export default Posts