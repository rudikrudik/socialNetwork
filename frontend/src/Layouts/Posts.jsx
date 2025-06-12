import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Post from "./Post";

function Posts(props) {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/user/posts/`],
        ([url]) => fetcherGet(url));

    if (isLoading) return <div>is loading</div>;
    if (error) return <div>is error</div>;

    return (
        <div className="main">
            <div>
                {data.map((item) => {
                    return <Post key={item[0]} data={item} user_prop={props.user}/>
                })}
            </div>
        </div>
    )
}

export default Posts