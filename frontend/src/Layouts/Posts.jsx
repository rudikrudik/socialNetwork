import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Post from "./Post";

function Posts() {
    const {
        data,
        isLoading
    } = useSWR([`${global.config.urls.baseUrl}/user/posts`],
        ([url]) => fetcherGet(url));

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