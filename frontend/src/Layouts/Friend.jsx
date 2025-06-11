import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Post from "./Post";

function Friend() {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/friends`],
        ([url]) => fetcherGet(url));

    if (isLoading) return <div>is loading</div>;
    if (error) {
        console.log(data);
        return <div>is error</div>;
    }


    return (
        <div className="main">
            <p>Friend</p>
        </div>
    )
}

export default Friend;