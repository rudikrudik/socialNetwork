import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import NewsPost from "./NewsPost";

function News() {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/post/feed/?post_limit=10&offset=0`],
        ([url]) => fetcherGet(url));

    if (isLoading) return <div>is loading</div>;
    if (error) return <div>is error</div>;

    console.log("News", data)

    return (
        <div className="main">
            <div>
                {data.map((item) => {
                    return <NewsPost key={item[0]} data={item}/>
                })}
            </div>
        </div>
    )
}

export default News;