import React from "react";
import useSWR from "swr";
import fetcher from "./FetcherData";
import '../config';

function Test(props) {
    const {
        data,
        error,
        isLoading
    } = useSWR(`${global.config.urls.baseUrl}/user/get/?id=1`, fetcher);
        //useSWR(`http://api.vsadmin.ru/user/get/?&id=1`, fetcher);

    if (error) return <p>Error Loading data</p>
    if (isLoading) return <p>Error Loading data</p>

    console.log({data})

    return (
        <div className="wrapper-card">
            <p>{data.id}</p>
            <p>{data.first_name}</p>
            <p>{data.last_name}</p>
            <p>{data.birthday}</p>
            <p>{data.gender}</p>
        </div>
    )
}

export default Test;