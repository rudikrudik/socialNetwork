import React from "react";
import useSWR from "swr";
import Cookies from "js-cookie";
import fetcher_cookie from "../Components/FetcherCookie";
import '../config';
import Post from "./Post";

function Posts () {
    const token = Cookies.get('user_access_token');

    const headers = {
        mode: "cors",
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        Cookies: `user_access_token=${token}`,
        'Content-Type': 'application/json'
    };
    const {
        data,
        isLoading
    } = useSWR([`${global.config.urls.baseUrl}/user/posts`, headers], ([url, headers]) => fetcher_cookie(url, headers));

    if (isLoading) return <div>is loading</div>;
    
    return (
        <div className="main">
            <div>
                {data.map((item) => {
                    return <Post key={item[0]} data={item}/>
                })}
            </div>
        </div>
    )
}

export default Posts