import React from "react";
import '../config';
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";
import Post from "./Post";
import Cookies from "js-cookie";

function Posts(props) {
    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/user/posts/`],
        ([url]) => fetcherGet(url));

    if (isLoading) return <div>is loading</div>;
    if (error) return <div>is error</div>;

    let ws = new WebSocket("ws://192.168.0.3:8001/ws");
    ws.onopen = function() {
        const user_id = Cookies.get('user_id');
        ws.send(JSON.stringify({ id_user: user_id }));
    };
    ws.onmessage = function(event) {
        //window.location.reload();
        alert(event.data);
    };


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