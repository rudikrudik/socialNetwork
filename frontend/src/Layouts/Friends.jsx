import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Friend from "./Friend";
import SearchFriends from "../Components/SearchFriends";

function Friends() {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/friends`],
        ([url]) => fetcherGet(url));

    if (isLoading) return <div>is loading</div>;
    if (error) {
        return <div>is error</div>;
    }

    return (
        <div className="main">
            <SearchFriends />
            {/*{data.map((item) => {
                    return <Friend key={item[0]} data={item}/>
                })*/}
        </div>
    )
}

export default Friends;