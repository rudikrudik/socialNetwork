import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Friend from "./Friend";

function Friends() {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/friends`],
        ([url]) => fetcherGet(url));

    console.log(data)

    if (isLoading) return <div>is loading</div>;
    if (error) {
        console.log(data);
        return <div>is error</div>;
    }


    return (
        <div className="main">
            <p>FRIENDS</p>
            <div>
                {data.map((item) => {
                    return <Friend key={item[0]} data={item}/>
                })}
            </div>
        </div>
    )
}

export default Friends;